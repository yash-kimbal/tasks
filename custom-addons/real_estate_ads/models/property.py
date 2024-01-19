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
    _name = 'estate.property'
    _description = 'Estate Property'

    # These will be the columns for our table.
    name = fields.Char(String="Name", required=True)
    tag_ids = fields.Many2many('estate.property.tag',String='Property Tag')
    type_id = fields.Many2one('estate.property.type', String='Property Type')
    description = fields.Text(String="Description")
    postcode = fields.Char(String="postcode")
    # data_availability = fields.Date(String="Available From", readonly=True)
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
                                          String="Garden Orientation", default='north')
    offer_ids = fields.One2many('estate.property.offer','property_id',String='Offers')
    sales_id = fields.Many2one('res.users', String="Salesman")
    buyer_id = fields.Many2one('res.partner', String="Buyer")
    # The second additional thing you should know are automatic fields
    # These fields are automatically created by odoo
    # They cannot be written to, but you can read them if you need to see some information there
    # And some of those fields are ID have an ID field that is an integer field which is unique
    # We have the crates Great Dates We have the great UI Which means who created this record
    # Each user created this record We also have write dates
    # The dates that this record was probably updated
    # Um, well, the last time it was modified
    # And we also have rights Uid these are the models that auto automatically creates for you
    # We see this when we have loaded this into our database
    # In the next lecture we will see how security play a big role in creating your model Get straight to that.
    # id,create_date,create_uid,write_date,write_uid


class PropertyType(models.Model):
    _name = 'estate.property.type'
    _description = 'Property Type'

    name = fields.Char(string="Name", required=True)


class PropertyTag(models.Model):
    _name = 'estate.property.tag'
    _description = 'Property Tags'

    name = fields.Char(string="Name", required=True)
