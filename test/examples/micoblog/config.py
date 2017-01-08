# _*_ coding: utf-8 _*_
SECRET_KEY = 'secret'
CSRF_ENABLED = True

OPENID_PROVIDERS = [{
    'name': 'Google',
    'url': 'https://www.google.com/accounts/o8/id'
}, {
    'name': 'Yahoo',
    'url': 'https://me.yahoo.com'
}, {
    'name': 'AOL',
    'url': 'http://openid.aol.com/<username>'
}, {
    'name': 'Flickr',
    'url': 'http://www.flickr.com/<username>'
}, {
    'name': 'MyOpenID',
    'url': 'https://www.myopenid.com'
}]
