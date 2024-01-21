from odoo import fields, models, api
from datetime import timedelta


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
            rec.validity = (rec.deadline - rec.creation_date).days
