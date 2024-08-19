import 'package:dartz/dartz.dart';
import 'package:spotify/core/usecase/usecase.dart';
import 'package:spotify/data/models/auth/check_user.dart';
import 'package:spotify/domain/repository/auth_repo/auth.dart';
import 'package:spotify/service_locator.dart';

class SigninUseCase implements UseCase<Either, CheckUser> {
  @override
  Future<Either> call({CheckUser? params}) {
    return serviceLocator<AuthRepository>().signin(params!);
  }
}
