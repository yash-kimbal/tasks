from odoo import fields, models, api
from datetime import timedelta
from odoo.exceptions import ValidationError


# Abstract Model:
#     Abstract models are generic models that implement certain features.
#     They are not intended to create a table in the database.
#     Example: The speaker creates an abstract model called abstract.offer with
#     fields like partner_email and partner_phone.
#     Regular models can inherit from abstract models to utilize their fields.
class AbstractOffer(models.AbstractModel):
    _name = 'abstract.model.offer'
    _description = 'Abstract Offers'

    partner_email = fields.Char(string="Email")
    partner_phone = fields.Char(string="Phone Number")


# Transient Model:
#     Transient models are used for wizard-style user interactions in Odoo.
#     The data stored in a transient model is temporary and expected to be cleaned up by the system.
#     Key attributes of transient models:
#     _transient (class attribute): Indicates that this is a transient model.
#     _transient_max_count:
#     Determines the maximum number of transient records in the database (set to zero for unlimited).
#     _transient_max_hours: Sets the maximum lifetime of transient records (set to zero for unlimited).
#     _transient_vacuum: A method that can be decorated with @api.autovacuum to clean up old records.
#
#     The speaker mentions an example of a transient model used in the Odoo system:
#     the "Import Translation" wizard, where users interact with a UI, perform operations,
#     and the data is stored temporarily.

# class TransientOffer(models.TransientModel):
#     _name = 'abstract.model.offer'
#     _description = 'Transient Offers'
#
#     @api.autovacuum
#     def _transient_vacuum(self):
#
#     partner_email = fields.Char(string="Email")
#     partner_phone = fields.Char(string="Phone Number")

# Regular Model:
#     Regular models are the common models used in Odoo, and they create tables in the database.
#     No specific example or demonstration is provided for regular models in this lecture,
#     but they have been extensively used in previous examples throughout the course.
class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _inherit = ['abstract.model.offer']
    _description = 'Estate Property Offers'

    @api.depends('property_id', 'partner_id')
    def _compute_name(self):
        for rec in self:
            if rec.property_id and rec.partner_id:
                rec.name = f"{rec.property_id.name} - {rec.partner_id.name}"
            else:
                rec.name = False

    name = fields.Char(string='Description', compute=_compute_name)
    price = fields.Float(string="Price")
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused')],
                              string="Status")
    partner_id = fields.Many2one('res.partner', string="Customer")
    property_id = fields.Many2one('estate.property', string="Property")
    validity = fields.Integer(string='Validity', default=7)
    deadline = fields.Date(string='Deadline', compute='compute_deadline', inverse='_inverse_deadline')

    #  The @api.model decorator is used for methods where self represents the model class, not an individual record.
    #  It simplifies operations that apply to the entire model without the need to loop through records.
    @api.model
    def _set_create_date(self):
        return fields.Date.today()

    creation_date = fields.Date(string='Create Date', default=_set_create_date)

    # COMPUTE --
    # Whereas in compute ,
    # it uses depends on decorator, and
    # it first loops over the self and takes compute and inverse as the parameter above.
    # it automatically calculates the value on the fly at moments.
    @api.depends('validity', 'creation_date')
    def compute_deadline(self):
        for rec in self:
            if rec.creation_date and rec.validity:
                rec.deadline = rec.creation_date + timedelta(days=rec.validity)
            else:
                rec.deadline = False

    # Here ,any change in the deadline will automatically change
    # the days(validity) only when the form is saved ,
    # not automatically without not saving the form.
    def _inverse_deadline(self):
        for rec in self:
            if rec.deadline and rec.creation_date:
                rec.validity = (rec.deadline - rec.creation_date).days
            else:
                rec.validity = False

    #  The @api.autovacuum decorator is used to define a method that gets invoked by the daily vacuum cron job.
    #  The cron job is responsible for cleaning up or deleting records based on specific conditions.
    # @api.autovacuum
    # def _clean_offers(self):
    #     self.search([('status','=','refused')]).unlink()

    # The @api.model_create_multi decorator is used for methods
    # that create multiple records from a list of dictionaries.
    # It allows for updates to value before record creation.
    # This example shows how to create multiple property records
    # with a default creation date if not specified in the input.

    # @api.model_create_multi
    # def create(self, vals):
    #     for rec in vals:
    #         if not rec.get('creation_date'):
    #             rec['creation_date'] = fields.Date.today()
    #     return super(PropertyOffer, self).create(vals)

    #     The @api.constraints decorator is used to prevent
    #     specific operations when certain conditions are not met.
    #     Constraints can be implemented either in Python or as SQL constraints.
    @api.constrains('validity')
    def _check_validity(self):
        for rec in self:
            if rec.deadline <= rec.creation_date:
                raise ValidationError("Deadline cannot be before creation date")

    # _sql_constraints = [
    #     ('check_validity','check(validity > 0','Deadline cannot be before creation date')
    # ]

    # @api.depends_context
    # allows specifying dependencies on context values in stored/computed methods.

    # Accept and Decline Buttons:
    #     Added "Accept" and "Decline" buttons to the offer view.
    #     Associated methods (action_accept and action_decline) to handle the logic when these buttons are clicked.
    #     Used icons and styles to make the buttons visually distinguishable.
    # Updating Selling Price on Accept:
    #     When an offer is accepted, the selling price of the associated property
    #     is updated to match the accepted offer's price.
    def action_accept_offer(self):
        if self.property_id:
            self._validate_accepted_offer()
            self.property_id.write({
                'selling_price': self.price,
                'state': 'accepted'
            })
        self.status = "accepted"

    # Validation on Acceptance:
    #     A validation method, validate_accepted_offer, is added to the offer model.
    #     It checks if there's already an accepted offer for the property and
    #     raises an error if attempting to accept another offer.
    #     After accepting an offer, the associated property is moved to the "Offer Accepted" state.
    def _validate_accepted_offer(self):
        offer_ids = self.env['estate.property.offer'].search([
            ('property_id', '=', self.property_id.id),
            ('status', '=', 'accepted'),
        ])

        if offer_ids:
            raise ValidationError("YOU HAVE AN ACCEPTED OFFER ALREADY")

    # Handling Decline:
    #
    #     On declining an offer, the associated property's selling price is set to zero,
    #     and the status is updated to "Received."
    def action_decline_offer(self):
        self.status = 'refused'
        if all(self.property_id.offer_ids.mapped('status')):
            self.property_id.write({
                'selling_price': 0,
                'state': 'received'
            })

    # Working with Server Actions

    def extend_offer_deadline(self):
        # Retrieves the list of active record IDs from the context.
        # The active_ids typically holds the IDs of records that the action is applied to.
        activ_ids = self._context.get('active_ids', [])
        if activ_ids:
            # Uses the Odoo environment (self.env) to create a
            # record set (offer_ids) for the model estate.property.offer using the active IDs.
            offer_ids = self.env['estate.property.offer'].browse(activ_ids)
            # Iterates through each record in the offer_ids record set.
            for offer in offer_ids:
                # Sets the validity field of each estate.property.offer record to the value of 10.
                offer.validity = 10

    # cron->Adding Scheduled Actions to our Module
    # search([]) -> Searching through all offers
    # search([()]) -> Want to have domain in this search function
    def _extend_offer_deadline(self):
        offer_ids = self.env['estate.property.offer'].search([])
        # So every day that this function runs, whatever value the offer validity is holding, it adds one to it.
        for offer in offer_ids:
            offer.validity = offer.validity + 1