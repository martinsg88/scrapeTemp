'use strict';

var tempShrineApp = angular.module('tempShrineApp', []);

tempShrineApp.controller('ShrineListController', function($scope, $http){
  $http({
    method: 'GET',
    url: 'infoFile'
  }).then(function (success){
	parseData(success.data); 
  },function (error){
	console.log(error);
  });

  function parseData(jsonData){
	console.log(jsonData);
  }


});