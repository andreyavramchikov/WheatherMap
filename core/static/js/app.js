'use strict'

var app = angular.module('weatherForecast', []);

app.config(function ($locationProvider, $httpProvider, $interpolateProvider) {

    $httpProvider.defaults.xsrfCookieName = 'csrftoken';
    $httpProvider.defaults.xsrfHeaderName = 'X-CSRFToken';

    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');

});