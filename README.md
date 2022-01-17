# RSS Ingestion

## About

This application downloads data from the endpoint `https://www.europarl.europa.eu/rss/doc/top-stories/` in the form of `csv` files to be stored in `AWS s3`.
It takes a parameter a list of xmls, that would represent different languages, for example:

```
'endpoints':[
      'https://www.europarl.europa.eu/rss/doc/top-stories/en.xml',
      'https://www.europarl.europa.eu/rss/doc/top-stories/es.xml',
      'https://www.europarl.europa.eu/rss/doc/top-stories/fr.xml',
      'https://www.europarl.europa.eu/rss/doc/top-stories/it.xml',
      ]
```

## Instalation

### Prerequisits

To deploy on AWS you will need