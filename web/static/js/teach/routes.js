var router = new (Backbone.Router.extend({
    routes: {
        '': 'showHome',
        'classes/create': 'createKlass',
        'classes/:id': 'showKlass',
        'classes/:class_id/students': 'showStudents',
        'classes/:class_id/students/add': 'addStudents',
        'classes/:class_id/students/:id': 'showStudentProfile'
    },

    showHome: function(){
        $('#app-body').empty();
        headerView.setTitle('Home');
        headerView.setButtons($('<a href="#classes/create" class="btn btn-ion btn-primary">Create</a>'))
    },

    createKlass: function(){
        $('#app-body').empty();
        (
            new CreateKlassView({model: new Klass()})
        ).$el.appendTo('#app-body');
    },

    showKlass: function(id){
        allKlasses.fetch().done(function(){
            var klass = allKlasses.get(id);
            klass.students.fetch().done(function() {
                $('#app-body').empty();
                headerView.setTitle(klass.toJSON().name);
                headerView.setButtons($('<a href="#classes/' + id + '/update" class="btn btn-ion btn-warning">Edit</a>'));
                (new KlassView({model: klass})).$el.appendTo('#app-body');
            });
        });
    },

    addStudents: function(){
        $('#app-body').empty();
        (
            new AddStudentsView({model: new Student()})
        ).$el.appendTo('#app-body');
    },

    showStudents: function(id){
        allKlasses.fetch().done(function(){
            var klass = allKlasses.get(id);
            klass.students.fetch().done(function(){
                $('#app-body').empty();
                headerView.setTitle(klass.toJSON().name);
                headerView.setButtons($('<a href="#classes/' + id + '/students/add" class="btn btn-ion btn-primary">Add</a>'));
                (new StudentsView({model: klass.students, klass_id: id})).$el.appendTo('#app-body');
            });
        });
    },

    showStudentProfile: function(class_id, student_id){
        allKlasses.fetch().done(function(){
            var klass = allKlasses.get(class_id);
            klass.students.fetch().done(function() {
                var student = klass.students.get(student_id);
                $('#app-body').empty();
                headerView.setTitle(klass.toJSON().name);
                headerView.setButtons('');
                (new StudentProfileView({model: student})).$el.appendTo('#app-body');
            });
        });
    }
}))();
