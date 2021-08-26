# Your_News
----
- a profiles api with authentication and profile feed functions
- each user needs to choose their prefrence of news type, which is serialized under a ProfileCategorySerializer
- whenver a profile's preference is updated or created through the profile api, articles are retrieved from the News API, and saved to the articles model in the db
- past articles retrieved are always stored within the db