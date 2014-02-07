var Klass = Backbone.Model.extend({
    defaults: {
        'name': 'Untitled class',
        'code': '',
        'start': '2014-01-01',
        'end': '2014-12-13',
        'colour': '#111111'
    }
});

var AllKlasses = Backbone.Collection.extend({
    model: Klass,
    url: '/api/klasses'
});
