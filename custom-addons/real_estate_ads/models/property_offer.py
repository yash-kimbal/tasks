from odoo import fields, models, api
from datetime import timedelta
from odoo.exceptions import ValidationError


class PropertyOffer(models.Model):
    _name = 'estate.property.offer'
    _description = 'Estate Property Offers'

    price = fields.Float(string="Price")
    status = fields.Selection([('accepted', 'Accepted'), ('refused', 'Refused')],
                              string="Status")
    partner_id = fields.Many2one('res.partner', string="Customer")
    property_id = fields.Many2one('estate.property', string="Property")
    validity = fields.Integer(string='Validity')
    deadline = fields.Date(string='Deadline', compute='compute_deadline', inverse='_inverse_deadline')

    #  The @api.model decorator is used for methods where self represents the model class, not an individual record.
    #  It simplifies operations that apply to the entire model without the need to loop through records.
    # @api.model()
    # def _set_create_date(self):
    #     return fields.Date.today()
    # creation_date = fields.Date(string='Create Date',default=_set_create_date)

    creation_date = fields.Date(string='Create Date')

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
    @api.model_create_multi
    def create(self, vals):
        for rec in vals:
            if not rec.get('creation_date'):
                rec['creation_date'] = fields.Date.today()
        return super(PropertyOffer, self).create(vals)

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
