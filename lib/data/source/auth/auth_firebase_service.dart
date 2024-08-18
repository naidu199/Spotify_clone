import 'package:firebase_auth/firebase_auth.dart';
import 'package:spotify/data/models/auth/new_user.dart';

abstract class AuthFirebase {
  Future<void> signup(NewUser newUser);
  Future<void> signin();
}

class AuthFirebaseService extends AuthFirebase {
  final FirebaseAuth firebaseAuth = FirebaseAuth.instance;
  @override
  Future<void> signin() {
    // TODO: implement signin
    throw UnimplementedError();
  }

  @override
  Future<void> signup(NewUser newUser) async {
    try {
      await firebaseAuth.createUserWithEmailAndPassword(
          email: newUser.email, password: newUser.password);
    } on FirebaseAuthException catch (e) {
      throw e.toString();
    }
  }
}
