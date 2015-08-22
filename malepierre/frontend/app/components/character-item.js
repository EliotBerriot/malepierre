import Ember from 'ember';

export default Ember.Component.extend({
    actions: {
        delete: function(character) {
            this.sendAction('delete', character);
        }
    }
});
