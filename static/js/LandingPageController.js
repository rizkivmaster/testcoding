// Global namespace
var LandingPageController = LandingPageController || {};

// Define constructor
LandingPageController = function() {
	this.name = "";
	this.email = "";
	this.message = "";

	this.SELECTOR = {
		NAME: "#name",
		EMAIL: "#email",
		MESSAGE: "#message",
		SUBMIT_BUTTON: "#submit-button"
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

	console.log("[Landing Page Controller] [Initialization]:", this);
};

LandingPageController.prototype.isValid = function(name, type, value){
	var self = this;

	// Required
	if(value == "" || value == null) {
		alert("Kami perlu tahu " + name + " Anda :)");
		return false;
	}	
	// Length Rule
	if(type == self.INPUT_TYPE.TEXT || type == self.INPUT_TYPE.EMAIL){
		if(type == self.INPUT_TYPE.TEXT && value.length < 4){
			alert(name + " Anda terlalu pendek, minimal 3 karakter ya :)");
			return false;
		}
		else if(type == self.INPUT_TYPE.EMAIL && value.length < 5){
			alert(name + " Anda terlalu pendek, minimal 5 karakter ya :)");
			return false;
		}	

		if(value.length > 30){
			alert(name + " Anda terlalu panjang, maksimal 30 karakter ya :)");
			return false;
		}
	} else if(type == self.INPUT_TYPE.TEXT_AREA){
		if(value.length < 16){
			alert(name + " Anda terlalu pendek, minimal 15 karakter ya :)");
			return false;
		}
		if(value.length > 1500){
			alert(name + " Anda terlalu panjang, maksimal 1500 karakter ya :)");
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

LandingPageController.prototype.cleanForm = function(){
	var self = this;
	
	self.name = $(self.SELECTOR.NAME).val("");
	self.email = $(self.SELECTOR.EMAIL).val("");
	self.message = $(self.SELECTOR.MESSAGE).val("");
};

LandingPageController.prototype.run = function(){
	var self = this;

	console.log("[Landing Page Controller] [Running..]:", self);

	self.cleanForm();

	$(self.SELECTOR.SUBMIT_BUTTON).click(function() {
		self.name = $(self.SELECTOR.NAME).val();
		self.email = $(self.SELECTOR.EMAIL).val();
		self.message = $(self.SELECTOR.MESSAGE).val();
	  	
	  	// Validate form
	  	var isValid = true;
	  	isValid = self.isValid("Nama", self.INPUT_TYPE.TEXT, self.name);
	  	if(isValid) isValid = self.isValid("Email", self.INPUT_TYPE.EMAIL, self.email);
	  	if(isValid) isValid = self.isValid("Pesan", self.INPUT_TYPE.TEXT_AREA, self.message);

	  	if(isValid){
			// Disable button
	  		$(this).attr("disabled", "disabled");
	  		
	  		var spec = {
	  			name: self.name,
	  			email: self.email,
	  			message: self.message
	  		};		

	  		console.log("[LandingPageController][Message Spec]", spec);

	  		// Call API here
	  		var request = $.ajax({
			  url: host_url+"/testimony/add",
			  type: "POST",
              contentType: "application/json; charset=utf-8",
			  data: JSON.stringify(spec),
			  dataType: "json"
			});
			 
			request.done(function(response) {
			  if(response["status"] == self.REQUEST_STATUS.SUCCESS) alert("Terima kasih! Pesan Anda sudah kami terima :)");
			  else alert("Pengiriman pesan gagal! Silakan coba lagi :)");
			  self.cleanForm();
			  // Enable button
	  		  $(self.SELECTOR.SUBMIT_BUTTON).removeAttr("disabled");
			});
			 
			request.fail(function(jqXHR, textStatus) {
			  alert("Pengiriman pesan gagal! Silakan coba lagi :)");
			  self.cleanForm();
			  // Enable button
	  		  $(self.SELECTOR.SUBMIT_BUTTON).removeAttr("disabled");
			});
	  	}

	});
};

var landingPage = new LandingPageController();
landingPage.run();

