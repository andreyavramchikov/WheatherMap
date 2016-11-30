"use strict";

var app = angular.module('weatherForecast');

app.controller('WheatherController', function ($scope, WheatherService) {
    $scope.city = 'Minsk';

    WheatherService.getForecast($scope.city).then(function (response) {
        $scope.data = response.data;
    });

    WheatherService.getCoordinates($scope.city).then(function (response) {
        var data = response.data;
        $scope.lon = data.lon;
        $scope.lat = data.lat;
    });

    WheatherService.getPressure($scope.city).then(function (response) {
        var data = response.data;
        $scope.pressures = _.map(data, 'pressure');
        $scope.labels = _.map(data, 'today_date');

    });
    WheatherService.getTemperature($scope.city).then(function (response) {
        var data = response.data;
        $scope.temp = {};
        $scope.temp.values = [_.map(data, 'temperature_day'), _.map(data, 'temperature_night')];
        $scope.temp.labels = _.map(data, 'today_date');
        $scope.series = ['Series A', 'Series B'];
    });

});
