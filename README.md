# Your_News

- a profiles django api with authentication and profile feed functions
- each user can choose their prefrence of news type
- articles are retrieved from another external api and stored within the articles model
- users can retrieve articles or create articles accordingly
- user feeds/comments for certain articles may be created or retrieved

# API/profiles
Users registration, selecting their preference of articles and account information
![profiles](/instances/profiles.png)

# API/articles
Any user (unauthorized) could create and access articles
![articles](/instances/articles.png)

# API/feed
Only authorized(logged in) users/admins can post comments toward each article
![articles](/instances/feed.png)
![admin](/instances/admin.png)

# Technologies
- Django
- Django REST Framework




