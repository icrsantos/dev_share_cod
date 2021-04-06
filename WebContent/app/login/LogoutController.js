app.controller('LogoutController', function (Auth, $state) {
    Auth.setUser(null);
    $state.go("home");
});