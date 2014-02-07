App = Ember.Application.create({});

App.ApplicationRoute = Ember.Route.extend({
    model: function() {
        return classes;
    }
});

App.Router.map(function() {
    this.route('index', { path: '/' });
    this.route('list', { path: '/list' });
    this.route('students', { path: '/students' });
    this.resource('student', { path: '/students/:student_id' });
});

/** demo stuff **/
App.IndexController = Ember.Controller.extend({
    message: 'Hello! See how index.hbs is evaluated in the context of IndexController'
});

App.ListRoute = Ember.Route.extend({
    setupController: function(controller) {
      controller.set('content', ['angular.js', 'backbone.js', 'ember.js']);
    }
});
/** end demo stuff **/

/** student stuff **/
App.StudentRoute = Ember.Route.extend({
    model: function() {
        // the model is an Array of all of the students
        return this.store.find('student');
    }
})

App.StudentRoute = Ember.Route.extend({
    model: function(params) {
        return this.store.find('student', params.student_id);
    },

    serialize: function(student){
        return {student_id: student.get('id') }:
    }
});













var classes = [
        {
            id: '1',
            name: 'Class #1',
        },
        {
            id: '2',
            name: 'Class #2',
        }
    ]

var students = [
    {
        id: '1',
        firstName: 'Hanjun',
        lastName: 'Kim',
        email: 'hanjun@kim.com'
    },
    {
        id: '2',
        firstName: 'Yunyi',
        lastName: 'Tang',
        email: 'yunyi@tang.com'
    }
]

var classes = [
    {
        id: '1',
        name: 'Class #1',
    },
    {
        id: '2',
        name: 'Class #2',
    }
]
