'use strict';

var tempShrineApp = angular.module('tempShrineApp', []);

tempShrineApp.controller('ShrineListController', function($scope, $http){
  $http({
    method: 'GET',
    url: 'infoFile'
  }).then(function (success){
	parseData(JSON.stringify(success.data), $scope); 
  },function (error){
	console.log(error);
  });

  function parseData(jsonData, $scope){
	var parsedJSON = JSON.parse(jsonData);
 	for(var key in parsedJSON){
		try{
			var test = JSON.parse(parsedJSON[key]);
			console.log(test);	
		}catch(e){
			//console.log(e);
		}
	}
  }
});
