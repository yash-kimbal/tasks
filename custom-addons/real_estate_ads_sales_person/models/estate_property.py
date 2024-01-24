from odoo import models, fields, api
from odoo.exceptions import ValidationError


class EstateProperty(models.Model):
    # The class EstateProperty is inheriting from the model "estate.property."
    # This means that it extends the functionality of the existing model.
    _inherit = "estate.property"

    # A new field sales_id of type Many2one is added to the inherited model.
    # It references the model "res.users" and is marked as required.
    sales_id = fields.Many2one("res.users", required=True, string="Salesman")

    # So what I want to do here is I want to ensure that only one property or two properties are assigned
    # to a user.
    # We cannot assign more than 1 or 2 properties to a user.
    # This decorator is used to override the create method when creating multiple records.
    @api.model_create_multi
    def create(self, vals_list):
        # The overridden create method checks each record's sales_id in the provided vals_list.
        for vals in vals_list:
            # For each record,
            # it counts the number of properties already assigned to the specified salesperson (sales_id).
            sales_person_property_ids = self.env[self._name].search_count([("sales_id", "=", vals.get("sales_id"))])
            if sales_person_property_ids >= 2:
                raise ValidationError("User already have enough property assigned to him.")
        # You can override the field by re-declaring the field and adding more field attributes,
        # or you can override a function by re-declaring the function without returning the super.
        # Or you can also return the super if you return the super.
        # It runs your block of code and also runs the super code or the super method code
        # if you don't return the super. You are basically replacing the function again.

        # If the validation passes,
        # the super() method is called to invoke the original create method of the inherited model.
        return super(EstateProperty, self).create(vals_list)
