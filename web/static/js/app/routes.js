var router = new (Backbone.Router.extend({
    routes: {
        '': 'showHome',
        'classes/:id': 'showKlass',
        'classes/:id/students': 'showStudents'
    },

    showHome: function(){
        console.log("TEST");
        $('#app-body').empty();
    },

    showKlass: function(id){
        allKlasses.fetch().done(function(){
            var klass = allKlasses.get(id);
            klass.students.fetch();
        });
    },

    showStudents: function(id){
        allKlasses.fetch().done(function(){
            console.log("Show students " + id);
            var klass = allKlasses.get(id);
            klass.students.fetch().done(function(){
                (new StudentsView({model: klass.students})).$el.appendTo('#app-body');
            });
        });
    }
}))();
