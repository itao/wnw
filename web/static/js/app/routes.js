var router = new (Backbone.Router.extend({
    routes: {
        '': 'showHome',
        'classes/create': 'createKlass',
        'classes/:id': 'showKlass',
        'classes/:id/students': 'showStudents'
    },

    showHome: function(){
        $('#app-body').empty();
        headerView.setTitle('Home');
        headerView.setButtons($('<a href="#classes/create" class="btn btn-ion btn-primary">Add class</a>'))
    },

    createKlass: function(){
        $('#app-body').empty();
        headerView.setTitle('Create Class');
        (
            new CreateKlassView({model: new Klass()})
        ).$el.appendTo('#app-body');
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
