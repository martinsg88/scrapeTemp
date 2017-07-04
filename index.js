'use strict';

var tempShrineApp = angular.module('tempShrineApp', []);

tempShrineApp.controller('ShrineListController', function($scope, $http){
  $http({
    method: 'GET',
    url: 'infoFile'
  }).then(function (success){
	parseData(success.data, $scope); 
  },function (error){
	console.log(error);
  });

  function parseData(jsonData, $scope){
	console.log(jsonData);
	var rawData = JSON.parse(jsonData); 
 	console.log(rawData); 
  }
});
