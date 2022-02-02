// ignore_for_file: prefer_const_constructors

import 'dart:convert';
import 'dart:developer';

import 'package:flutter/material.dart';
import 'package:flutter_app/information.dart';
import 'package:flutter_app/pages/login_page.dart';
import 'package:shared_preferences/shared_preferences.dart';

void main(){
  runApp(MyApp());



}

class MyApp extends StatelessWidget {
 //final String url  ="http://192.168.93.35:8080";
   String url = "http://thrallweb.fr:8080";
 information infos = information();

 MyApp({Key? key}) {

    getData();
 }
void getData ()async{
   log("iciiiiii");
   SharedPreferences prefs = await SharedPreferences.getInstance();
   var jsonInfo = prefs.getString("infos");
   if(jsonInfo !=null){
     infos.fromJson(json.decode(jsonInfo));
     log(jsonInfo);
   }
}



  @override
  Widget build(BuildContext context) {
    return MaterialApp(
        title: "login",
        home : login(url : url, infos : infos)
    );
  }
}
