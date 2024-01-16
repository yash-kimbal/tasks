# A model is a class that maps to a data relation.
# It will include all the necessary fields and behaviors for the data you will be storing.
# The _name attribute is most required as it defines the name of the model.
# It`s the table.
from odoo import fields, models


class Property(models.Model):
    # We create our table.
    # I name it.States.Property.
    # This will be the model and this will be translated to state underscore property in our table.
    # In Odoo we use dots.
    # That 's how you define the model.
    _name = 'estate.property',

    # These will be the columns for our table.
    name = fields.Char(String="Name")
    description = fields.Text(String="Description")
    postcode = fields.Char(String="postcode")
    data_availability = fields.Date(String="Available From")
    expected_price = fields.Float(String="Expected Price")
    best_offer = fields.Float(String="Best Offer")
    selling_price = fields.Float(String="Selling Price")
    bedrooms = fields.Integer(String="Bedrooms")
    living_area = fields.Integer(String="Living Area(sqm)")
    facades = fields.Integer(String="Facades")
    garage = fields.Boolean(String="Garage", default=False)
    garden = fields.Boolean(String="Garden", default=False)
    garden_area = fields.Integer(String="Garden Area")
    garden_orientation = fields.Selection([('north', 'North'), ('south', 'South'), ('east', 'East'), ('west', 'West')],
                                          String="Garden Orientation")
