"use strict";

var app = angular.module('weatherForecast');

app.controller('WheatherController', function ($scope, WheatherService) {
    $scope.first = 'asdfasdf';
    WheatherService.getForecast().then(function(response){
        $scope.data = response.data;
    });
});
