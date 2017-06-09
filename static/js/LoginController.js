// Global namespace
var LoginController = LoginController || {};

// Define constructor
LoginController = function() {
	this.username = "";
	this.password = "";

	this.SELECTOR = {
		USERNAME: "#username",
		PASSWORD: "#password",
		LOGIN_BUTTON: "#login-btn"
	};

	this.INPUT_TYPE = {
		TEXT: "text",
		TEXT_AREA: "textarea",
		EMAIL: "email"
	};

	this.REQUEST_STATUS = {
		SUCCESS: "SUCCESS",
		FAILED: "FAILED"
	};

	console.log("[Login Controller] [Initialization]:", this);
};

LoginController.prototype.isValid = function(name, type, value){
	var self = this;

	// Required
	if(value == "" || value == null) {
		alert("Kami harus tahu " + name + " Anda :)");
		return false;
	}	
	// Length Rule
	if(type == self.INPUT_TYPE.TEXT || type == self.INPUT_TYPE.EMAIL){
		if(type == self.INPUT_TYPE.TEXT && value.length < 4){
			alert(name + " Anda terlalu pendek, minimal 3 karakter yah :)");
			return false;
		}
		else if(type == self.INPUT_TYPE.EMAIL && value.length < 5){
			alert(name + " Anda terlalu pendek, minimal 5 karakter yah :)");
			return false;
		}	

		if(value.length > 30){
			alert(name + " Anda terlalu panjang, maksimal 30 karakter yah :)");
			return false;
		}
	} else if(type == self.INPUT_TYPE.TEXT_AREA){
		if(value.length < 16){
			alert(name + " Anda terlalu pendek, minimal 15 karakter yah :)");
			return false;
		}
		if(value.length > 1500){
			alert(name + " Anda terlalu panjang, maksimal 1500 karakter yah :)");
			return false;
		}
	}
	
	// Email Rule	
	if(type == self.INPUT_TYPE.EMAIL){
	    var patt = /^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;
	    if(!patt.test(value)) alert("Format " + name + " Anda salah :)");
	    return patt.test(value);
	}

	return true;
};

LoginController.prototype.cleanForm = function(){
	var self = this;
	
	self.username = $(self.SELECTOR.USERNAME).val("");
	self.password = $(self.SELECTOR.PASSWORD).val("");
};

LoginController.prototype.run = function(){
	var self = this;

	console.log("[Login Controller] [Running..]:", self);

	self.cleanForm();

	$(self.SELECTOR.LOGIN_BUTTON).click(function() {
		self.username = $(self.SELECTOR.USERNAME).val();
		self.password = $(self.SELECTOR.PASSWORD).val();
	  	
	  	// Validate form
	  	var isValid = true;
	  	isValid = self.isValid("Username", self.INPUT_TYPE.TEXT, self.username);
	  	if(isValid) isValid = self.isValid("Password", self.INPUT_TYPE.TEXT, self.password);

	  	if(isValid){
			// Disable button
			// Uncomment this if API ready
	  		//$(this).attr("disabled", "disabled");
	  		
	  		var spec = {
	  			username: self.username,
	  			password: self.password
	  		};		

	  		console.log("[LoginController][Login Spec]", spec);

	  		// Call API here
	  		// Uncomment this if API ready
	  		/*var request = $.ajax({
			  url: host_url+"/testimony/add",
			  type: "POST",
              contentType: "application/json; charset=utf-8",
			  data: JSON.stringify(spec),
			  dataType: "json"
			});
			 
			request.done(function(response) {
			  if(response["status"] == self.REQUEST_STATUS.SUCCESS) alert("Redirect to Admin Page..");
			  else alert("Wahai saudaraku, cracking itu merupakan dosa besar, taubatlah kau.");
			  self.cleanForm();
			  // Enable button
	  		  $(self.SELECTOR.LOGIN_BUTTON).removeAttr("disabled");
			});
			 
			request.fail(function(jqXHR, textStatus) {
			  alert("Wahai saudaraku, cracking itu merupakan dosa besar, taubatlah kau.");
			  self.cleanForm();
			  // Enable button
	  		  $(self.SELECTOR.LOGIN_BUTTON).removeAttr("disabled");
			});*/
	  	}

	});
};

var loginController = new LoginController();
loginController.run();

