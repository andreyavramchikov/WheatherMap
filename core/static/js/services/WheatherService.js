"use strict";


var app = angular.module('weatherForecast');


app.service('WheatherService', function ($http) {

    this.getForecast = function (city) {
        return $http.get('/api/' + city + '/forecast/');
    };

    this.getPressure = function(city){
        return $http.get('/api/' + city + '/pressure/');
    };

    this.getTemperature = function(city){
        return $http.get('/api/' + city + '/temperature/');
    };

    this.getCoordinates = function(city){
        return $http.get('/api/' + city + '/');
    }

});