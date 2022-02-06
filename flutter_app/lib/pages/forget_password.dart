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
  bool hidePassword = true;
  bool rememberMe = false;
  TextEditingController _emailCo = TextEditingController();
  TextEditingController _pswdCo = TextEditingController();




  void snackBarMessage(String msg){
    ScaffoldMessenger.of(context).showSnackBar(SnackBar(
      content:  Text(msg),
      duration: const Duration(seconds: 5),
      // action: SnackBarAction(
      //   label: 'ACTION',
      //   onPressed: () { },
      // ),
    ));
  }

  void loginRequest() async{
    try {
      var response = await post(Uri.parse(widget.url+"/login"),body: {
        "email" : _emailCo.text,
        "password" : _pswdCo.text
      });
      log(response.body);

      print(response.body);

      if(response.statusCode==200){
        widget.infos.connexion(jsonDecode(response.body), _emailCo.text,  _pswdCo.text);
        widget.infos.print();
        if(rememberMe) {
          log(json.encode(widget.infos.toJson()));
          widget.infos.updateJson();

          //prefs.setString("infos", json.encode(widget.infos.toJson()));
          // prefs.setString("email", _emailCo.text);
          // prefs.setString("password", _pswdCo.text);
        }
        else {
          //   prefs.remove("email");
          //   prefs.remove("password");
          //
          // prefs.remove("infos");
          widget.infos.deleteJson();
        }

        Navigator.push(context, MaterialPageRoute(builder: (context)=> computer_chose(url : widget.url, infos : widget.infos)));


        return;
      }else{
        snackBarMessage(jsonDecode(response.body)["message"]);
        return;
      }
    } catch (err) {
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
          // Navigator.of(context).(MaterialPageRoute(
          //     builder: (context)=>Remote()
          // ))
          print(_emailCo.text+" "+_pswdCo.text),
          if(EmailValidator.Validate(_emailCo.text,context) && PasswordValidator.Validate(_pswdCo.text, context)){
            loginRequest()
          }

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
