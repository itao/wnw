var MainNavView = Backbone.HandlebarsView.extend({
    tagName: 'nav',
    className: 'side-nav',
    id: 'main-nav',

    events: {
        'click .side-nav-back': 'back',
        'click .klass .side-nav-open': 'selectKlass',
        'click .students': 'selectStudents',
        //'click .settings': 'selectStudents',
        //'click .schedules': 'selectStudents',
    },

    initialize: function(){
        var self = this;
        self.listenTo(self.model, "add remove", function(){
            self.model.each(function(klass){
                self.listenTo(klass, "change", self.render);
                self.listenTo(klass.students, "add remove", self.render);
            });
            self.render();
        });
    },

    selectKlass: function(event){
        var id = $(event.currentTarget).closest('*[data-id]').attr('data-id');
        this.model.each(function(k){k.set('selected',false)});
        this.model.get(id).set('selected',true);
        router.navigate('classes/' + id, {trigger: true});
    },

    selectStudents: function(event){
        var id = $(event.currentTarget).closest('*[data-id]').attr('data-id');
        router.navigate('classes/' + id + '/students', {trigger: true});
        return false;
    },

    back: function(){
        this.model.each(function(k){k.set('selected',false)});
        router.navigate('', {trigger: true});
    },

    template: $('#main-nav-template').html()
})

var mainNav = new MainNavView({
    el: $("#main-nav"),
    model: allKlasses
});

var StudentsView = Backbone.HandlebarsView.extend({

    initialize: function(){
        this.render();
    },

    template: $('#students-template').html()
});