import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';

void main() {
  runApp(MyApp());
}

abstract class ModelEvent {
  @override
  String toString() => '$runtimeType{}';
}

abstract class ModelState {
  @override
  String toString() => '$runtimeType{}';
}

class FetchEvent extends ModelEvent {}

class UninitializedState extends ModelState {}

class LoadingState extends ModelState {}

class ErrorState extends ModelState {}

class LoadedState extends ModelState {}

class ModelRepository {
  Future<void> doSomeThing() async {
    await new Future.delayed(new Duration(minutes: 2));
  }
}

class ModelBloc extends Bloc<ModelEvent, ModelState> {
  final ModelRepository? repository;

  ModelBloc({
    this.repository,
  }) : super(UninitializedState());
  @override
  Stream<ModelState> mapEventToState(ModelEvent event) async* {
    // yield UninitializedState();
    if (event is FetchEvent) {
      yield* _mapFetchEventToState(event);
    }
  }

  Stream<ModelState> _mapFetchEventToState(
    FetchEvent fetchEvent,
  ) async* {
    try {
      yield LoadingState();
      await repository?.doSomeThing();
      yield LoadedState();
    } catch (e) {
      yield ErrorState();
    }
  }
}

class LoadingWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Column(
        mainAxisAlignment: MainAxisAlignment.center,
        children: <Widget>[
          const CircularProgressIndicator(strokeWidth: 1.5),
          const SizedBox(height: 16),
          Text(
            'Loading...',
            style: Theme.of(context).textTheme.subtitle1,
          ),
        ],
      ),
    );
  }
}

class EmptyWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text(
        "🌴",
        style: Theme.of(context).textTheme.headline4,
      ),
    );
  }
}

class ErrorWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text(
        "❌",
        style: Theme.of(context).textTheme.headline4,
      ),
    );
  }
}

class ResultWidget extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Center(
      child: Text(
        "⭕",
        style: Theme.of(context).textTheme.headline4,
      ),
    );
  }
}

class ModelBlocWidget extends StatefulWidget {
  @override
  State<StatefulWidget> createState() => _ModelBlocWidgetState();
}

class _ModelBlocWidgetState extends State<ModelBlocWidget> {
  final ModelBloc _modelBloc = ModelBloc(repository: ModelRepository());

  @override
  void initState() {
    super.initState();
    _modelBloc.add(FetchEvent());
  }

  @override
  void dispose() {
    _modelBloc.close();
    super.dispose();
  }

  Widget _mapWidgetState(final BuildContext context, final ModelState state) {
    if (state is UninitializedState) {
      return EmptyWidget();
    }
    if (state is LoadingState) {
      return LoadingWidget();
    }
    if (state is ErrorState) {
      return ErrorWidget();
    }
    if (state is LoadedState) {
      return ResultWidget();
    }
    return EmptyWidget();
  }

  @override
  Widget build(BuildContext context) {
    return BlocProvider(
      create: (BuildContext context) => _modelBloc,
      child: BlocListener<ModelBloc, ModelState>(
        listener: (context, state) {
          print(state.toString());
        },
        child: BlocBuilder<ModelBloc, ModelState>(
          builder: (context, state) => _mapWidgetState(context, state),
        ),
      ),
    );
  }
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Flutter Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: MyHomePage(title: 'Flutter Demo Home Page'),
    );
  }
}

class MyHomePage extends StatefulWidget {
  MyHomePage({Key? key, this.title}) : super(key: key);

  final String? title;

  @override
  _MyHomePageState createState() => _MyHomePageState();
}

class _MyHomePageState extends State<MyHomePage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(widget.title!),
      ),
      body: ModelBlocWidget(),
      floatingActionButton: FloatingActionButton(
        onPressed: _incrementCounter,
        tooltip: 'Increment',
        child: Icon(Icons.add),
      ),
    );
  }
}
