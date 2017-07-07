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
 	$scope.arrayOfShrines = [];	
	for(var key in parsedJSON){
		try{
			$scope.arrayOfShrines.push(JSON.parse(parsedJSON[key]));
		}catch(e){
			//console.log(e);
		}
	}
	$scope.stamps = $scope.arrayOfShrines[2].Specialties2;
  }
});
