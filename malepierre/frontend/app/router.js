import Ember from 'ember';
import config from './config/environment';

var Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
    this.resource('characters', function() {
        this.route('create');
        this.resource('character', {path: ':character_id' }, function(){
            this.route('edit');
        });
    });
});

export default Router;
