var Klass = Backbone.Model.extend({
    defaults: {
        'name': 'Untitled class',
        'code': '',
        'start': '2014-01-01',
        'end': '2014-12-13',
        'colour': '#111111',
        'selected': false,
    },

    initialize: function() {
        this.students = new StudentsInKlass();
        this.students.klass = this;
    }
});

var AllKlasses = Backbone.Collection.extend({
    model: Klass,
    url: '/api/klasses'
});

var allKlasses = new AllKlasses();

var Student = Backbone.Model.extend({
    defaults: {},
    url: '/api/students/:id'
})

var StudentsInKlass = Backbone.Collection.extend({
    model: Student,
    url: function() {
        return this.klass.url() + '/students'
    }
})
