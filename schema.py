from marshmallow import Schema, fields

class TestPropertySchema(Schema):
  id = fields.Int(required=True)
  property_name = fields.Str()
  address = fields.Str()
  description = fields.Str()
  beds = fields.Int()
  baths = fields.Int()
  sqft = fields.Int()

class TestListingSchema(TestPropertySchema):
  id = fields.int(required=True)
  property_id = fields.Int(required=True)
  listing_title = fields.Str()
  listing_price = fields.Int()
  zestimate = fields.Int()
  est_payment = fields.Int()
  est_rent = fields.Int()
  rent = fields.Int()

