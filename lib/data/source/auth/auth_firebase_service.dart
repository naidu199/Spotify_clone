import 'package:dartz/dartz.dart';
import 'package:firebase_auth/firebase_auth.dart';
import 'package:spotify/data/models/auth/check_user.dart';
import 'package:spotify/data/models/auth/new_user.dart';

abstract class AuthFirebase {
  Future<Either> signup(NewUser newUser);
  Future<Either> signin(CheckUser user);
}

class AuthFirebaseService extends AuthFirebase {
  final FirebaseAuth firebaseAuth = FirebaseAuth.instance;
  @override
  Future<Either> signin(CheckUser user) async {
    try {
      await firebaseAuth.signInWithEmailAndPassword(
          email: user.email, password: user.password);
      return const Right('Success');
    } on FirebaseAuthException catch (e) {
      String res = '';

      if (e.code == 'invalid-email') {
        res = 'Not user found for that email';
      } else if (e.code == 'invalid-credential') {
        res = 'Wrong password provided for that user';
      }

      return Left(res);
    }
  }

  @override
  Future<Either> signup(NewUser newUser) async {
    try {
      await firebaseAuth.createUserWithEmailAndPassword(
          email: newUser.email, password: newUser.password);
      return const Right('Success');
    } on FirebaseAuthException catch (e) {
      String res = '';

      if (e.code == 'weak-password') {
        res = 'The password provided is too weak';
      } else if (e.code == 'email-already-in-use') {
        res = 'An account already exists with that email.';
      }

      return Left(res);
    }
  }
}
