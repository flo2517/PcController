// ignore_for_file: prefer_const_literals_to_create_immutables, prefer_const_constructors

import 'dart:convert';
import 'dart:developer';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter_app/pages/control_page.dart';
import 'package:flutter_app/pages/sign_in.dart';
import 'package:http/http.dart';

import '../information.dart';
import '../input_validator.dart';

class editDevice extends StatefulWidget {
  final String url;
  information infos;
  editDevice({
    Key? key,
    required this.url,
    required this.infos

  }) : super(key: key);

  @override
  _editDevice createState() => _editDevice();
}

class _editDevice extends State<editDevice> {

  TextEditingController _Name = TextEditingController();

  @override
  void initState() {
    _Name.text= widget.infos.computerName!;

  }

  //TextEditingController _username = TextEditingController();

  /// i = 1 => rename
  /// i= 2 => delete
  void Request(int i) async {
    var response;
    switch(i){
      case 1 :
         response = await post(Uri.parse(widget.url+"/device/update"),  headers: {"x-access-token": widget.infos.token}, body: {
          "uuid": widget.infos.computerId,
          "name": _Name.text
        });
        log( widget.infos.computerId);
        if(response.statusCode == 200){
          showAlertDialog(context, "Succes","Rename",sign: true, rename: true);


        }
        log(response.statusCode.toString());
        log(response.body);

        break;
      case 2 :
        response = await post(Uri.parse(widget.url+"/device/delete"),  headers: {"x-access-token": widget.infos.token}, body: {
          "uuid": widget.infos.computerId,
        });
        if(response.statusCode == 200){
          showAlertDialog(context, "Succes","Delete",sign: true, rename: true);
        }

        break;
      default :
        break;
    }

    // log(widget.url);
    // log(response.statusCode.toString());
    log(response.body);
    //
    if(response.statusCode != 200){
      snackBarMessage(jsonDecode(response.body)["message"]);
    }



  }
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
  Widget buildRename() {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: <Widget>[
        Text(
          'Rename device',
          style: TextStyle(
              color: Colors.white, fontSize: 16, fontWeight: FontWeight.bold),
        ),
        SizedBox(height: 10),
        Container(
          alignment: Alignment.centerLeft,
          decoration: BoxDecoration(
              color: Colors.white,
              borderRadius: BorderRadius.circular(10),
              boxShadow: [
                BoxShadow(
                    color: Colors.black26, blurRadius: 6, offset: Offset(0, 2))
              ]),
          height: 60,
          child: TextField(
            controller: _Name,
            keyboardType: TextInputType.emailAddress,
            style: TextStyle(color: Colors.black87),
            decoration: InputDecoration(
                border: InputBorder.none,
                contentPadding: EdgeInsets.only(top: 14),
                prefixIcon: Icon(Icons.edit_outlined, color: Colors.blue),
                hintStyle: TextStyle(color: Colors.black26)),
          ),
        )
      ],
    );
  }
  //
  Widget buildRenameBtn() {
    return Container(
      padding: EdgeInsets.symmetric(vertical: 25),
      width: double.infinity,
      child: RaisedButton(
        elevation: 5,
        onPressed: () => {
          // // Navigator.of(context).(MaterialPageRoute(
          // //     builder: (context)=>Remote()
          // // ))
          // print(_Name.text + " " + _pswdCo.text ),
          // if(EmailValidator.Validate(_Name.text,context) && PasswordValidator.Validate(_pswdCo.text, context)){
          //   signInRequest()
          // }
          // //Navigator.push(context, MaterialPageRoute(builder: (context)=> Remote()))
          Request(1)
        },
        padding: EdgeInsets.all(15),
        shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(15)),
        color: Colors.white,
        child: Text(
          'Rename',
          style: TextStyle(
              color: Colors.blue, fontSize: 18, fontWeight: FontWeight.bold),
        ),
      ),
    );
  }

  Widget buildDeleteBtn() {
    return GestureDetector(
      onTap: () => {
Request(2)
      },
      child: RichText(
          text: TextSpan(
              text: "Delete device",
              style: TextStyle(
                  color: Colors.yellowAccent,
                  fontSize: 18,
                  fontWeight: FontWeight.w500))),
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
                        ])),
                child: SingleChildScrollView(
                  padding: EdgeInsets.symmetric(horizontal: 25, vertical: 120),
                  child: Column(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: <Widget>[
                      Text(
                        "Edit device",
                        style: TextStyle(
                            color: Colors.white,
                            fontSize: 40,
                            fontWeight: FontWeight.bold),
                      ),
                      SizedBox(height: 50),
                      buildRename(),
                      // buildUsername(),
                      // SizedBox(height: 20),


                      // buildForgotPassBtn(),
                      // buildRemember(),
                      buildRenameBtn(),
                      buildDeleteBtn()
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
