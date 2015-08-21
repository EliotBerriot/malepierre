import Ember from 'ember';
import config from './config/environment';

var Router = Ember.Router.extend({
  location: config.locationType
});

Router.map(function() {
  this.resource('characters', { path: '/' });
  this.route('characters');
});

export default Router;
