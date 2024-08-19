import 'package:get_it/get_it.dart';
import 'package:spotify/data/repository/auth/auth_repo_impl.dart';
import 'package:spotify/data/source/auth/auth_firebase_service.dart';
import 'package:spotify/domain/repository/auth_repo/auth.dart';
import 'package:spotify/domain/usecases/auth/signin.dart';
import 'package:spotify/domain/usecases/auth/signup.dart';

final serviceLocator = GetIt.instance;

Future<void> initializeDependencies() async {
  serviceLocator.registerSingleton<AuthFirebase>(
    AuthFirebaseService(),
  );
  serviceLocator.registerSingleton<AuthRepository>(
    AuthRepoImpl(),
  );
  serviceLocator.registerSingleton<SignupUseCase>(
    SignupUseCase(),
  );
  serviceLocator.registerSingleton<SigninUseCase>(
    SigninUseCase(),
  );
}
