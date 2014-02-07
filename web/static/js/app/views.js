var headerView = new (Backbone.View.extend({
    initialize: function() {
        this.render()
    },

    setTitle: function(title){
        this.title = title;
        this.render();
    },

    setButtons: function(buttons){
        this.buttons = buttons;
        this.render();
    },

    render: function(){
        this.$('#content-title').empty().append(this.title);
        this.$('#header-actions').empty().append(this.buttons);
        return this;
    }
}))({el:$('header.content-header')})

var MainNavView = Backbone.HandlebarsView.extend({
    tagName: 'nav',
    className: 'side-nav',
    id: 'main-nav',

    events: {
        'click .side-nav-back': 'back',
        'click .home': 'home',
        'click .klass .side-nav-open': 'selectKlass',
        'click .overview': 'showKlass',
        'click .students': 'showStudents',
        //'click .settings': 'showStudents',
        //'click .schedules': 'showStudents',
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
    },

    showKlass: function(event){
        var id = $(event.currentTarget).closest('*[data-id]').attr('data-id');
        router.navigate('classes/' + id, {trigger: true});
        return false;
    },

    showStudents: function(event){
        var id = $(event.currentTarget).closest('*[data-id]').attr('data-id');
        router.navigate('classes/' + id + '/students', {trigger: true});
        return false;
    },

    back: function(){
        this.model.each(function(k){k.set('selected',false)});
    },

    home: function() {
        router.navigate('', {trigger: true});
    },

    template: $('#main-nav-template').html()
})

var mainNav = new MainNavView({
    el: $("#main-nav"),
    model: allKlasses
});

var CreateKlassView = Backbone.HandlebarsView.extend({

    initialize: function(){
        _.bindAll(this,'save');
        this.render();
    },

    template: $('#create-klass-template').html(),

    save: function(){
        form = this.$('#add-class-form');
        classname = form.find('input[name=classname]').val();
        dates = form.find('input[name=classdaterangepicker]').val();
        colour = form.find('select[name=class-colour-picker]').val();
        dates = dates.split(' - ');

        var convertDateFormat = function(dateString) {
            date = new Date(dateString);
            newString = date.getFullYear() + '-' + date.getMonth() + '-' + date.getDate();
            return newString;
        };

        start = convertDateFormat(dates[0]);
        end = convertDateFormat(dates[1]);
        allKlasses.add(this.model);
        this.model.save({
            'name' : classname,
            'start' : start,
            'end'   : end,
            'teacher' : 21,
            'colour': colour
        });
    },

    render: function(){
        headerView.setTitle('Create a class');
        headerView.setButtons($('<a href="#" class="btn btn-ion btn-success">Save</a>').on('click', this.save));
        Backbone.HandlebarsView.prototype.render.call(this);

        this.$('#classdaterangepicker').daterangepicker(
            {
                format: 'YYYY-MM-DD',
                buttonClasses: 'btn btn-ion'
            }
        );

        // colorpicker
        this.$('#class-colour-picker').simplecolorpicker({
            theme: 'glyphicons'
        });

        /*
        this.$('#add-class-form').validate({
            errorElement: 'div',
            errorClass: 'help-block',
            focusInvalid: false,
            rules: {
                classname : {
                    required: true,
                },
            },
            messages: {
                classname : {
                    required: "Please provide a class name."
                },
            }
        });
        */
    }
});


var KlassView = Backbone.HandlebarsView.extend({
    initialize: function(){
        this.render();
    },

    template: $('#klass-overview-template').html()
});

var StudentsView = Backbone.HandlebarsView.extend({

    events: {
        'click .student': 'showStudentProfile',
    },

    initialize: function(options){
        this.options = options;
        this.render();
    },

    showStudentProfile: function(event){
        var klass_id  = this.options.klass_id
        var student_id = $(event.currentTarget).closest('*[data-id]').attr('data-id');
        router.navigate('classes/' + klass_id + '/students/' + student_id, {trigger: true});
        return false;
    },

    template: $('#students-template').html()
});

var StudentProfileView = Backbone.HandlebarsView.extend({
    initialize: function(){
        var self = this;
        self.listenTo(self.model, "change", self.render);
        this.render();
    },

    template: $('#student-profile-template').html()
})