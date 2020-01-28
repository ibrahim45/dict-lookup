# dict-lookup

This utility tool help to search meaning of word in terminal.


# prerequisties

We are using owl bot dictionary API (that provides free api)

```
https://owlbot.info
```

# setup

```
pip install dict-lookup
```

Get api token from registered email on clicking `get a free token` in owlbot site.

```
export OWL_API_TOKEN=<value> 
```
*** please save the api token permanently, in path variables/system variables of your machine ***

Type below command in terminal,

```
dict challenge
```

Response will be in the format of 

```
{   u'definitions': [   {   u'definition': u'a call to prove or justify something.',
                            u'emoji': None,
                            u'example': u'a <b>challenge to</b> the legality of the banning order',
                            u'image_url': None,
                            u'type': u'noun'},
                        {   u'definition': u'a call to someone to participate in a competitive situation or fight to decide who is superior in terms of ability or strength.',
                            u'emoji': None,
                            u'example': u'he accepted the challenge',
                            u'image_url': None,
                            u'type': u'noun'}],
    u'pronunciation': None,
    u'word': u'challenge'

}
```

