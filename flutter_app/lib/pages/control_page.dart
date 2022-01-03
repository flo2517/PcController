
import 'dart:convert';
import 'dart:developer';

import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart';

void main() => runApp(MyApp());

class MyApp extends StatefulWidget {
  @override
  State<MyApp> createState() => _MyAppState();
}

class _MyAppState extends State<MyApp> {
  @override
  Widget build(BuildContext context) {
    return const MaterialApp(title: 'Controleur de pc', home: Remote());
  }
}


//void main() => runApp(const MaterialApp(title: 'Controleur de pc', home: Remote()));

// class MyApp extends StatelessWidget {
//   @override
//   Widget build(BuildContext context) {
//     return const
//   }
// }




class Remote extends StatefulWidget {
  const Remote({Key? key}) : super(key: key);

  @override
  State<Remote> createState() => _RemoteState();
}

class _RemoteState extends State<Remote> {
  String label = "label ici";
  final id = 1234;

  final url ="http://192.168.156.232:8080";

  Future<String> fetchPosts(String request) async{

    try{
      final response= await get(Uri.parse(url+request));
      final jsonData = jsonDecode(response.body);
      log("success");
      log(response.statusCode.toString());
      log(response.body);
      log(jsonData["message"]);
      return jsonData["message"] +" - code : "+response.statusCode.toString();

    }catch(err){
      log(err.toString());
      return err.toString();

    }

  }

  /// state : 1- up , 2-down, 3-mute, 4-unmute, 5-play, 6-pause , 7-shutdown
  void requete(int state) async {
    String message="";
    String request= "";
    switch (state) {
      case 1 :
        message = "up - ";
        request = "/volume/up/"+id.toString();
        break;
      case 2:
        request = "/volume/down/"+id.toString();
        message = "down - ";

        break;
      case 3 :
        request = "/volume/mute/"+id.toString();
        message = "mute - ";

        break;
      case 4 :
        request = "/volume/unmute/"+id.toString();
        message = "unmute - ";

        break;
      case 5 :
        request = "/volume/play/"+id.toString();
        message = "play - ";

        break;
      case 6:
        request = "/volume/pause/"+id.toString();
        message = "pause - ";

        break;
      case 7 :
        request = "/shutdown/"+id.toString();
        message = "shutdown - ";

        break;
      default :
        break;

    }
    message += await fetchPosts(request);

    setState(() {
      label = message;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Pc controller'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.start,
          children: [
            SizedBox(
              height: 100,
              ///volume
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: <Widget>[
                  Transform.scale(
                    scale: 3,
                    child: IconButton(
                      icon: const Icon(Icons.volume_off_rounded),
                      onPressed: () {
                        requete(3);
                      },
                    ),
                  ),
                  Transform.scale(
                    scale: 3,
                    child: IconButton(
                      icon: const Icon(Icons.volume_down_rounded),
                      onPressed: () {
                        requete(2);

                      },
                    ),
                  ),
                  Transform.scale(
                    scale: 3,
                    child: IconButton(
                      icon: const Icon(Icons.volume_up_rounded),
                      onPressed: () {
                        requete(1);

                      },
                    ),
                  ),
                ],
              ),
            ), //Controle du volume
            SizedBox(
              height: 100,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Transform.scale(
                    scale: 3,
                    child: IconButton(
                      icon: const Icon(Icons.play_circle_outline_rounded),
                      onPressed: () {
                        requete(5);

                      },
                    ),
                  ),
                  Transform.scale(
                    scale: 3,
                    child: IconButton(
                      icon: const Icon(Icons.pause_circle_outline_rounded),
                      onPressed: () {
                        requete(6);

                      },
                    ),
                  ),
                ],
              ),
            ), //play pause
            SizedBox(
              height: 100,
              child: Row(
                mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                children: [
                  Transform.scale(
                    scale: 3,
                    child: IconButton(
                      icon: const Icon(Icons.lock_outline_rounded),
                      onPressed: () {},
                    ),
                  ),
                  Transform.scale(
                    scale: 3,
                    child: IconButton(
                      icon: const Icon(Icons.power_settings_new_rounded),
                      onPressed: () {
                        requete(7);

                        // showDialog(
                        //     context: context,
                        //     barrierDismissible: false,
                        //
                        //     builder: (_) =>
                        //         CupertinoAlertDialog(
                        //           title: Text("clique"),
                        //           //content: Text("fezgzge"),
                        //           actions:
                        //             <Widget>[
                        //               CupertinoDialogAction(
                        //                 child: Text('ok'),
                        //                 onPressed: () {
                        //                   Navigator.of(context).pop();
                        //                 },
                        //               ),
                        //
                        //             ],
                        //
                        //         )
                        // );

                      },
                    ),
                  ),
                ],
              ),
            ),//
            SizedBox(height: 10.0),
            Text(
                '$label',
                style: TextStyle(
                    fontSize: 20
                )

            )

          ],

        ),
      ),
    );
  }
}
