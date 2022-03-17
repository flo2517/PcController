// ignore_for_file: prefer_const_literals_to_create_immutables, prefer_const_constructors

import 'dart:convert';
import 'dart:developer';



import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_app/information.dart';
import 'package:flutter_app/input_validator.dart';
import 'package:flutter_app/pages/computer_chose.dart';
import 'package:flutter_app/pages/control_page.dart';
import 'package:flutter_app/pages/sign_in.dart';
import 'package:http/http.dart';
import 'package:shared_preferences/shared_preferences.dart';

class forgotPass extends StatefulWidget {
  final String url;
  information infos;
  // login({Key? key}) :

  forgotPass({
    Key? key,
    required this.url,
    required this.infos
  }) : super(key: key);

  @override
  _forgotPassState createState() => _forgotPassState();
}

class _forgotPassState extends State<forgotPass> {

  TextEditingController _emailCo = TextEditingController();


  void snackBarMessage(String msg){
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(
      content:  Text(msg),
      duration: const Duration(seconds: 5),

    ));
  }

  void resetPassRequest() async{
    try {
      var response = await post(Uri.parse(widget.url+"/resetPasswordMail"),body: {
        "email" : _emailCo.text

      });
      log(response.body);
      snackBarMessage(jsonDecode(response.body)["message"]);

        return;
      }
     catch (err) {
      log(err.toString());

    }
  }


  Widget buildResetBtn(){
    return Container(
      padding: EdgeInsets.symmetric(vertical: 25),
      width: double.infinity,
      child: RaisedButton(
        elevation: 5,
        onPressed: ()=> {
          resetPassRequest()

        } ,
        padding: EdgeInsets.all(15),
        shape: RoundedRectangleBorder(
            borderRadius: BorderRadius.circular(15)
        ),
        color: Colors.white,
        child: Text(
          'Send email to reset',
          style: TextStyle(
              color : Colors.blue,
              fontSize: 18,
              fontWeight: FontWeight.bold
          ),
        ) ,
      ),
    );
  }
  Widget buildEmail (){
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Text(
          'Email',
          style:TextStyle(
              color: Colors.white,
              fontSize: 16,
              fontWeight: FontWeight.bold
          ),
        ),
        SizedBox(height: 10),
        Container(
          alignment: Alignment.centerLeft,
          decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(10),
              boxShadow: [
                BoxShadow(
                    color: Colors.black26,
                    blurRadius: 6,
                    offset: Offset(0,2)
                )
              ]

          ),
          height: 60,
          child: TextField(

            controller: _emailCo,
            keyboardType: TextInputType.emailAddress,
            style: TextStyle(
                color: Colors.black87
            ),
            decoration: InputDecoration(
                border: InputBorder.none,
                contentPadding: EdgeInsets.only(top: 14),
                prefixIcon: Icon(
                    Icons.email,
                    color: Colors.blue
                ),
                hintText: 'Email',
                hintStyle: TextStyle(
                    color: Colors.black26

                )
            ),
          ),
        )
      ],
    );
  }
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: AnnotatedRegion<SystemUiOverlayStyle>(
        value: SystemUiOverlayStyle.light,
        child: GestureDetector(
          child: Stack(
            children: <Widget>[
              Container(
                height: double.infinity,
                width: double.infinity,
                decoration: BoxDecoration(
                    gradient: LinearGradient(
                        begin: Alignment.topCenter,
                        end: Alignment.bottomCenter,
                        colors: [
                          Colors.blue,
                          Colors.blue[300]!,
                          Colors.blue[100]!,

                        ]
                    )
                ),
                child: SingleChildScrollView(

                  padding: EdgeInsets.symmetric(
                      horizontal: 25,
                      vertical: 120
                  ),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: <Widget>[
                      Text(
                        "Reset password ?",
                        style : TextStyle(
                            color : Colors.white,
                            fontSize: 40,
                            fontWeight: FontWeight.bold
                        ),
                      ),
                      SizedBox(height: 50),
                      buildEmail(),
                      buildResetBtn(),

                    ],
                  ),
                ),
              )
            ],
          ),
        ),
      ),
    );
  }
}
