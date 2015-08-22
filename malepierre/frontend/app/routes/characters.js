import Ember from 'ember';

export default Ember.Route.extend({
    model: function() {
        return this.store.findAll('character');
    },
    actions: {
        delete: function(character) {
            character.destroyRecord();
            this.transitionTo('characters');
        },
        create: function(name) {
            // Create the new Todo model
            var character = this.store.createRecord('character', {
                name: name,
            });

            this.controllerFor('characters').set('name', '');

            // Save the new model
            character.save();
            // router.transitionTo('somewhere');
        }
    }
});
