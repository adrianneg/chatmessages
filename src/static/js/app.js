var chatApp = angular.module("chatApp", []);

chatApp.controller("messageCtrl", ["$scope", "$http", function($scope, $http){

  $scope.messages = [];

  $http.get("/messages/api/?format=json")
   .then(function(response) {
       $scope.messages = response.data;
   });

  $scope.saveMessage = function(){
    var msg = $scope.newmessage;
    $scope.messages.push({text: msg, done: false});
    $scope.newmessage = "";
    return;
  };

  $scope.removeMessage = function(){
    var messages = [];
    angular.forEach($scope.messages, function(message, i) {
        if(!message.done) {
           messages.push(message);
        }
    });

    $scope.messages = messages;
  };

}]);
