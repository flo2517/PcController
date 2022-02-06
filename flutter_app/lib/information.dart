import 'dart:convert';
import 'dart:developer';

import 'package:shared_preferences/shared_preferences.dart';

class information {

   String? email;
   String? password;
   bool isConnected = false;
   var token;



   var refreshToken;
   var computerId;

   void setToken(token){
      this.token = token;
   }

   void connexion (json, email, password){
      this.email = email;
      this.password = password;
      token = json["token"];
      refreshToken = json["refreshToken"];
      isConnected = true;
   }
   void deconnexion(){
      email=null;
      password = null;
      token = null;
      refreshToken = null;
      isConnected = false;
   }
   void print(){
      log("email : "+email!+"\nmdp : "+password!+"\nIsConnected : "+isConnected.toString()+"\nToken : "+token+"\nRefreshToken : "+refreshToken.toString());
   }
   Map<String, dynamic> toJson() => {
      'email': email,
      'password': password,
      'isConnected': isConnected,
      'token' : token,
      'refreshToken' : refreshToken,
      'computerId' : computerId
   };

   void fromJson(Map<String, dynamic> json){
      email = json['email'];
      password = json['password'];
      isConnected = json['isConnected'];
      token = json['token'];
      refreshToken = json['refreshToken'];
      computerId = json['computerId'];

   }

   void updateJson () async{
      SharedPreferences prefs = await SharedPreferences.getInstance();
      prefs.setString("infos", json.encode(toJson()));
   }

   void deleteJson() async {
      SharedPreferences prefs = await SharedPreferences.getInstance();
      prefs.remove("infos");
   }




}