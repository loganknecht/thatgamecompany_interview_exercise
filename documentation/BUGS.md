# Trailing Slash Required in Requests URL
`settings.py` property `APPEND_NEW_SLASH` should capture routes without a trailing slash and if not matched against any other routes, should be retried with a `/`.

This is not working correctly at the moment

`~/api/v1/ping` != `~/api/v1/ping/` at the moment and it should be fixed, otherwise requests without a trailing slash will fail

# Migrate the User model
User mode is stored at the top level of the api and the appropriate location seems as though it should be in `api/versions/v1`

I'm not familiar enough with django conventions so I am unsure if the project needs to be restructured or if the settings of the django project need to be changed for the user overwrite.

Either way a restructuring will need to be redone.

# Django Best Practices - File Structure
Look into if the file structure is reflective of what people typically do for best practices

# API
## Prevent duplicates from being made of items somehow?
- /shop/items - POST endpoint should do some level of deduplication, maybe?

## Decouple the price of an item by abstracting with a shop
Right now the item value and the price are tightly coupled. What it should be, is that a shope contains items, that have value, but the shops values are variable. By having the price on the item object it provides no mechanism to create a variable set of prices on a per shop and per item basis.

Move it out to a shop interface.

# Security
## Need to evaluate how much sensitive information is being exposed
There may be some exposure of player ids in queries where it is not relevant.

Make sure that the information is filtered approriately.

