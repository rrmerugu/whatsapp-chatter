
'use strict';
var app = angular.module('app',['ngResource', 'ngRoute']);

// override the angular print function
app.config(['$interpolateProvider',function ($interpolateProvider) {
    $interpolateProvider.startSymbol('[[');
    $interpolateProvider.endSymbol(']]');
}]);


app.config(['$resourceProvider', function($resourceProvider) {
  // Don't strip trailing slashes from calculated URLs
  $resourceProvider.defaults.stripTrailingSlashes = false;
}]);




app.controller('baseController', [ '$rootScope', '$scope', '$http',    function (  $rootScope, $scope, $http) {

$scope.searchKw = "";

$scope.loadChat = function(page){

      var request = $http({
            method: "get",
            url: "/api/beta0.6/chat/list?page="+page ,
        });
        request.success(function (data) {
            console.log(data);
            if (data.previous != null){
            $scope.prev = data.previous.split("=")[1];
            }

            if (data.next != null){
                $scope.next = data.next.split("=")[1];
            }

            $scope.messages = data.results;
        }).error(function (data) {
            console.log(data);
        });
};
$scope.loadChat(1);


    $scope.searchWord = function(){
    console.log("Search the Word");
     var kw = $scope.searchKw;
          var request = $http({
                method: "get",
                url: "/api/beta0.6/chat/list?message="+kw ,
            });
            request.success(function (data) {
                console.log(data);
                if (data.previous != null){
                $scope.prev = data.previous.split("=")[1];
                }

                if (data.next != null){
                    $scope.next = data.next.split("=")[1];
                }

                $scope.messages = data.results;
            }).error(function (data) {
                console.log(data);
            });


    };


    $scope.getBufferMessages = function(message_id, page){


    console.log("Gathering buffer messages for message id "+ message_id + "&page="+ page);


         var elements = document.getElementsByClassName("search-result-message") ;

          for (var i = 0; i < elements.length; i++) {
                elements[i].style.backgroundColor="#fff";
            }



    document.getElementById("search-message-id-"+message_id).style.backgroundColor="#efefef";

          var request = $http({
                method: "get",
                url: "/api/beta0.6/chat/buffer?message_id="+message_id+ "&page="+ page ,
            });
            request.success(function (data) {
                console.log(data);
                if (data.previous != null){
                    $scope.buf_previous = data.previous.split("&page=")[1];
                    console.log($scope.buf_previous);
                }
                else{
                $scope.buf_previous = 0;
                }

                if (data.next != null){
                    $scope.buf_next = data.next.split("&page=")[1];
                    console.log($scope.buf_next);
                }else{
                $scope.buf_next  = 0
                }
                $scope.buffer_message_id = message_id;

                $scope.buffer_messages = data.results;
            }).error(function (data) {
                console.log(data);
            });

    };



}]);