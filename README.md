# CatchPoint Usage Scraper

CatchPoint doesn't allow you to grab your point usage via their API. This container login and scrape the Activity page and returns *Points Used* and *Contracted Monthly*. (This could be extended to scrape more values, but were not needed for my purposes) The scraped values are returned via STDOUT; which (in my case) are captured by Jenkins then displayed in a graph.

## Run the Container:

```
docker run --rm \
-e CPUSER=user@example.com \
-e CPPASS=super-secret-password \
brycetho/docker-soup
```

### Environment Variables:
**CPUSER**: Username for CatchPoint account

**CPPASS**: Password for CatchPoint account
