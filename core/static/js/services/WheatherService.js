"use strict";


var app = angular.module('weatherForecast');


app.service('WheatherService', function ($http) {

    this.getForecast = function () {
        return $http.get('/api/forecast/');
    };
});