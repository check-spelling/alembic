# ### this file stubs are generated by tools/write_pyi.py - do not edit ###
# ### imports are manually managed

from typing import Callable
from typing import ContextManager
from typing import Optional
from typing import TextIO
from typing import Tuple
from typing import TYPE_CHECKING
from typing import Union

if TYPE_CHECKING:
    from sqlalchemy.engine.base import Connection
    from sqlalchemy.sql.schema import MetaData

    from .migration import MigrationContext
    from .runtime.migration import _ProxyTransaction

### end imports ###

def begin_transaction() -> Union["_ProxyTransaction", ContextManager]:
    """Return a context manager that will
    enclose an operation within a "transaction",
    as defined by the environment's offline
    and transactional DDL settings.

    e.g.::

        with context.begin_transaction():
            context.run_migrations()

    :meth:`.begin_transaction` is intended to
    "do the right thing" regardless of
    calling context:

    * If :meth:`.is_transactional_ddl` is ``False``,
      returns a "do nothing" context manager
      which otherwise produces no transactional
      state or directives.
    * If :meth:`.is_offline_mode` is ``True``,
      returns a context manager that will
      invoke the :meth:`.DefaultImpl.emit_begin`
      and :meth:`.DefaultImpl.emit_commit`
      methods, which will produce the string
      directives ``BEGIN`` and ``COMMIT`` on
      the output stream, as rendered by the
      target backend (e.g. SQL Server would
      emit ``BEGIN TRANSACTION``).
    * Otherwise, calls :meth:`sqlalchemy.engine.Connection.begin`
      on the current online connection, which
      returns a :class:`sqlalchemy.engine.Transaction`
      object.  This object demarcates a real
      transaction and is itself a context manager,
      which will roll back if an exception
      is raised.

    Note that a custom ``env.py`` script which
    has more specific transactional needs can of course
    manipulate the :class:`~sqlalchemy.engine.Connection`
    directly to produce transactional state in "online"
    mode.

    """

def configure(
    connection: Optional["Connection"] = None,
    url: Optional[str] = None,
    dialect_name: Optional[str] = None,
    dialect_opts: Optional[dict] = None,
    transactional_ddl: Optional[bool] = None,
    transaction_per_migration: bool = False,
    output_buffer: Optional[TextIO] = None,
    starting_rev: Optional[str] = None,
    tag: Optional[str] = None,
    template_args: Optional[dict] = None,
    render_as_batch: bool = False,
    target_metadata: Optional["MetaData"] = None,
    include_name: Optional[Callable] = None,
    include_object: Optional[Callable] = None,
    include_schemas: bool = False,
    process_revision_directives: Optional[Callable] = None,
    compare_type: bool = False,
    compare_server_default: bool = False,
    render_item: Optional[Callable] = None,
    literal_binds: bool = False,
    upgrade_token: str = "upgrades",
    downgrade_token: str = "downgrades",
    alembic_module_prefix: str = "op.",
    sqlalchemy_module_prefix: str = "sa.",
    user_module_prefix: Optional[str] = None,
    on_version_apply: Optional[Callable] = None,
    **kw
) -> None:
    """Configure a :class:`.MigrationContext` within this
    :class:`.EnvironmentContext` which will provide database
    connectivity and other configuration to a series of
    migration scripts.

    Many methods on :class:`.EnvironmentContext` require that
    this method has been called in order to function, as they
    ultimately need to have database access or at least access
    to the dialect in use.  Those which do are documented as such.

    The important thing needed by :meth:`.configure` is a
    means to determine what kind of database dialect is in use.
    An actual connection to that database is needed only if
    the :class:`.MigrationContext` is to be used in
    "online" mode.

    If the :meth:`.is_offline_mode` function returns ``True``,
    then no connection is needed here.  Otherwise, the
    ``connection`` parameter should be present as an
    instance of :class:`sqlalchemy.engine.Connection`.

    This function is typically called from the ``env.py``
    script within a migration environment.  It can be called
    multiple times for an invocation.  The most recent
    :class:`~sqlalchemy.engine.Connection`
    for which it was called is the one that will be operated upon
    by the next call to :meth:`.run_migrations`.

    General parameters:

    :param connection: a :class:`~sqlalchemy.engine.Connection`
     to use
     for SQL execution in "online" mode.  When present, is also
     used to determine the type of dialect in use.
    :param url: a string database url, or a
     :class:`sqlalchemy.engine.url.URL` object.
     The type of dialect to be used will be derived from this if
     ``connection`` is not passed.
    :param dialect_name: string name of a dialect, such as
     "postgresql", "mssql", etc.
     The type of dialect to be used will be derived from this if
     ``connection`` and ``url`` are not passed.
    :param dialect_opts: dictionary of options to be passed to dialect
     constructor.

     .. versionadded:: 1.0.12

    :param transactional_ddl: Force the usage of "transactional"
     DDL on or off;
     this otherwise defaults to whether or not the dialect in
     use supports it.
    :param transaction_per_migration: if True, nest each migration script
     in a transaction rather than the full series of migrations to
     run.
    :param output_buffer: a file-like object that will be used
     for textual output
     when the ``--sql`` option is used to generate SQL scripts.
     Defaults to
     ``sys.stdout`` if not passed here and also not present on
     the :class:`.Config`
     object.  The value here overrides that of the :class:`.Config`
     object.
    :param output_encoding: when using ``--sql`` to generate SQL
     scripts, apply this encoding to the string output.
    :param literal_binds: when using ``--sql`` to generate SQL
     scripts, pass through the ``literal_binds`` flag to the compiler
     so that any literal values that would ordinarily be bound
     parameters are converted to plain strings.

     .. warning:: Dialects can typically only handle simple datatypes
        like strings and numbers for auto-literal generation.  Datatypes
        like dates, intervals, and others may still require manual
        formatting, typically using :meth:`.Operations.inline_literal`.

     .. note:: the ``literal_binds`` flag is ignored on SQLAlchemy
        versions prior to 0.8 where this feature is not supported.

     .. seealso::

        :meth:`.Operations.inline_literal`

    :param starting_rev: Override the "starting revision" argument
     when using ``--sql`` mode.
    :param tag: a string tag for usage by custom ``env.py`` scripts.
     Set via the ``--tag`` option, can be overridden here.
    :param template_args: dictionary of template arguments which
     will be added to the template argument environment when
     running the "revision" command.   Note that the script environment
     is only run within the "revision" command if the --autogenerate
     option is used, or if the option "revision_environment=true"
     is present in the alembic.ini file.

    :param version_table: The name of the Alembic version table.
     The default is ``'alembic_version'``.
    :param version_table_schema: Optional schema to place version
     table within.
    :param version_table_pk: boolean, whether the Alembic version table
     should use a primary key constraint for the "value" column; this
     only takes effect when the table is first created.
     Defaults to True; setting to False should not be necessary and is
     here for backwards compatibility reasons.
    :param on_version_apply: a callable or collection of callables to be
        run for each migration step.
        The callables will be run in the order they are given, once for
        each migration step, after the respective operation has been
        applied but before its transaction is finalized.
        Each callable accepts no positional arguments and the following
        keyword arguments:

        * ``ctx``: the :class:`.MigrationContext` running the migration,
        * ``step``: a :class:`.MigrationInfo` representing the
          step currently being applied,
        * ``heads``: a collection of version strings representing the
          current heads,
        * ``run_args``: the ``**kwargs`` passed to :meth:`.run_migrations`.

    Parameters specific to the autogenerate feature, when
    ``alembic revision`` is run with the ``--autogenerate`` feature:

    :param target_metadata: a :class:`sqlalchemy.schema.MetaData`
     object, or a sequence of :class:`~sqlalchemy.schema.MetaData`
     objects, that will be consulted during autogeneration.
     The tables present in each :class:`~sqlalchemy.schema.MetaData`
     will be compared against
     what is locally available on the target
     :class:`~sqlalchemy.engine.Connection`
     to produce candidate upgrade/downgrade operations.
    :param compare_type: Indicates type comparison behavior during
     an autogenerate
     operation.  Defaults to ``False`` which disables type
     comparison.  Set to
     ``True`` to turn on default type comparison, which has varied
     accuracy depending on backend.   See :ref:`compare_types`
     for an example as well as information on other type
     comparison options.

     .. seealso::

        :ref:`compare_types`

        :paramref:`.EnvironmentContext.configure.compare_server_default`

    :param compare_server_default: Indicates server default comparison
     behavior during
     an autogenerate operation.  Defaults to ``False`` which disables
     server default
     comparison.  Set to  ``True`` to turn on server default comparison,
     which has
     varied accuracy depending on backend.

     To customize server default comparison behavior, a callable may
     be specified
     which can filter server default comparisons during an
     autogenerate operation.
     defaults during an autogenerate operation.   The format of this
     callable is::

        def my_compare_server_default(context, inspected_column,
                    metadata_column, inspected_default, metadata_default,
                    rendered_metadata_default):
            # return True if the defaults are different,
            # False if not, or None to allow the default implementation
            # to compare these defaults
            return None

        context.configure(
            # ...
            compare_server_default = my_compare_server_default
        )

     ``inspected_column`` is a dictionary structure as returned by
     :meth:`sqlalchemy.engine.reflection.Inspector.get_columns`, whereas
     ``metadata_column`` is a :class:`sqlalchemy.schema.Column` from
     the local model environment.

     A return value of ``None`` indicates to allow default server default
     comparison
     to proceed.  Note that some backends such as Postgresql actually
     execute
     the two defaults on the database side to compare for equivalence.

     .. seealso::

        :paramref:`.EnvironmentContext.configure.compare_type`

    :param include_name: A callable function which is given
     the chance to return ``True`` or ``False`` for any database reflected
     object based on its name, including database schema names when
     the :paramref:`.EnvironmentContext.configure.include_schemas` flag
     is set to ``True``.

     The function accepts the following positional arguments:

     * ``name``: the name of the object, such as schema name or table name.
       Will be ``None`` when indicating the default schema name of the
       database connection.
     * ``type``: a string describing the type of object; currently
       ``"schema"``, ``"table"``, ``"column"``, ``"index"``,
       ``"unique_constraint"``, or ``"foreign_key_constraint"``
     * ``parent_names``: a dictionary of "parent" object names, that are
       relative to the name being given.  Keys in this dictionary may
       include:  ``"schema_name"``, ``"table_name"``.

     E.g.::

        def include_name(name, type_, parent_names):
            if type_ == "schema":
                return name in ["schema_one", "schema_two"]
            else:
                return True

        context.configure(
            # ...
            include_schemas = True,
            include_name = include_name
        )

     .. versionadded:: 1.5

     .. seealso::

        :ref:`autogenerate_include_hooks`

        :paramref:`.EnvironmentContext.configure.include_object`

        :paramref:`.EnvironmentContext.configure.include_schemas`


    :param include_object: A callable function which is given
     the chance to return ``True`` or ``False`` for any object,
     indicating if the given object should be considered in the
     autogenerate sweep.

     The function accepts the following positional arguments:

     * ``object``: a :class:`~sqlalchemy.schema.SchemaItem` object such
       as a :class:`~sqlalchemy.schema.Table`,
       :class:`~sqlalchemy.schema.Column`,
       :class:`~sqlalchemy.schema.Index`
       :class:`~sqlalchemy.schema.UniqueConstraint`,
       or :class:`~sqlalchemy.schema.ForeignKeyConstraint` object
     * ``name``: the name of the object. This is typically available
       via ``object.name``.
     * ``type``: a string describing the type of object; currently
       ``"table"``, ``"column"``, ``"index"``, ``"unique_constraint"``,
       or ``"foreign_key_constraint"``
     * ``reflected``: ``True`` if the given object was produced based on
       table reflection, ``False`` if it's from a local :class:`.MetaData`
       object.
     * ``compare_to``: the object being compared against, if available,
       else ``None``.

     E.g.::

        def include_object(object, name, type_, reflected, compare_to):
            if (type_ == "column" and
                not reflected and
                object.info.get("skip_autogenerate", False)):
                return False
            else:
                return True

        context.configure(
            # ...
            include_object = include_object
        )

     For the use case of omitting specific schemas from a target database
     when :paramref:`.EnvironmentContext.configure.include_schemas` is
     set to ``True``, the :attr:`~sqlalchemy.schema.Table.schema`
     attribute can be checked for each :class:`~sqlalchemy.schema.Table`
     object passed to the hook, however it is much more efficient
     to filter on schemas before reflection of objects takes place
     using the :paramref:`.EnvironmentContext.configure.include_name`
     hook.

     .. seealso::

        :ref:`autogenerate_include_hooks`

        :paramref:`.EnvironmentContext.configure.include_name`

        :paramref:`.EnvironmentContext.configure.include_schemas`

    :param render_as_batch: if True, commands which alter elements
     within a table will be placed under a ``with batch_alter_table():``
     directive, so that batch migrations will take place.

     .. seealso::

        :ref:`batch_migrations`

    :param include_schemas: If True, autogenerate will scan across
     all schemas located by the SQLAlchemy
     :meth:`~sqlalchemy.engine.reflection.Inspector.get_schema_names`
     method, and include all differences in tables found across all
     those schemas.  When using this option, you may want to also
     use the :paramref:`.EnvironmentContext.configure.include_name`
     parameter to specify a callable which
     can filter the tables/schemas that get included.

     .. seealso::

        :ref:`autogenerate_include_hooks`

        :paramref:`.EnvironmentContext.configure.include_name`

        :paramref:`.EnvironmentContext.configure.include_object`

    :param render_item: Callable that can be used to override how
     any schema item, i.e. column, constraint, type,
     etc., is rendered for autogenerate.  The callable receives a
     string describing the type of object, the object, and
     the autogen context.  If it returns False, the
     default rendering method will be used.  If it returns None,
     the item will not be rendered in the context of a Table
     construct, that is, can be used to skip columns or constraints
     within op.create_table()::

        def my_render_column(type_, col, autogen_context):
            if type_ == "column" and isinstance(col, MySpecialCol):
                return repr(col)
            else:
                return False

        context.configure(
            # ...
            render_item = my_render_column
        )

     Available values for the type string include: ``"column"``,
     ``"primary_key"``, ``"foreign_key"``, ``"unique"``, ``"check"``,
     ``"type"``, ``"server_default"``.

     .. seealso::

        :ref:`autogen_render_types`

    :param upgrade_token: When autogenerate completes, the text of the
     candidate upgrade operations will be present in this template
     variable when ``script.py.mako`` is rendered.  Defaults to
     ``upgrades``.
    :param downgrade_token: When autogenerate completes, the text of the
     candidate downgrade operations will be present in this
     template variable when ``script.py.mako`` is rendered.  Defaults to
     ``downgrades``.

    :param alembic_module_prefix: When autogenerate refers to Alembic
     :mod:`alembic.operations` constructs, this prefix will be used
     (i.e. ``op.create_table``)  Defaults to "``op.``".
     Can be ``None`` to indicate no prefix.

    :param sqlalchemy_module_prefix: When autogenerate refers to
     SQLAlchemy
     :class:`~sqlalchemy.schema.Column` or type classes, this prefix
     will be used
     (i.e. ``sa.Column("somename", sa.Integer)``)  Defaults to "``sa.``".
     Can be ``None`` to indicate no prefix.
     Note that when dialect-specific types are rendered, autogenerate
     will render them using the dialect module name, i.e. ``mssql.BIT()``,
     ``postgresql.UUID()``.

    :param user_module_prefix: When autogenerate refers to a SQLAlchemy
     type (e.g. :class:`.TypeEngine`) where the module name is not
     under the ``sqlalchemy`` namespace, this prefix will be used
     within autogenerate.  If left at its default of
     ``None``, the ``__module__`` attribute of the type is used to
     render the import module.   It's a good practice to set this
     and to have all custom types be available from a fixed module space,
     in order to future-proof migration files against reorganizations
     in modules.

     .. seealso::

        :ref:`autogen_module_prefix`

    :param process_revision_directives: a callable function that will
     be passed a structure representing the end result of an autogenerate
     or plain "revision" operation, which can be manipulated to affect
     how the ``alembic revision`` command ultimately outputs new
     revision scripts.   The structure of the callable is::

        def process_revision_directives(context, revision, directives):
            pass

     The ``directives`` parameter is a Python list containing
     a single :class:`.MigrationScript` directive, which represents
     the revision file to be generated.    This list as well as its
     contents may be freely modified to produce any set of commands.
     The section :ref:`customizing_revision` shows an example of
     doing this.  The ``context`` parameter is the
     :class:`.MigrationContext` in use,
     and ``revision`` is a tuple of revision identifiers representing the
     current revision of the database.

     The callable is invoked at all times when the ``--autogenerate``
     option is passed to ``alembic revision``.  If ``--autogenerate``
     is not passed, the callable is invoked only if the
     ``revision_environment`` variable is set to True in the Alembic
     configuration, in which case the given ``directives`` collection
     will contain empty :class:`.UpgradeOps` and :class:`.DowngradeOps`
     collections for ``.upgrade_ops`` and ``.downgrade_ops``.  The
     ``--autogenerate`` option itself can be inferred by inspecting
     ``context.config.cmd_opts.autogenerate``.

     The callable function may optionally be an instance of
     a :class:`.Rewriter` object.  This is a helper object that
     assists in the production of autogenerate-stream rewriter functions.

     .. seealso::

         :ref:`customizing_revision`

         :ref:`autogen_rewriter`

         :paramref:`.command.revision.process_revision_directives`

    Parameters specific to individual backends:

    :param mssql_batch_separator: The "batch separator" which will
     be placed between each statement when generating offline SQL Server
     migrations.  Defaults to ``GO``.  Note this is in addition to the
     customary semicolon ``;`` at the end of each statement; SQL Server
     considers the "batch separator" to denote the end of an
     individual statement execution, and cannot group certain
     dependent operations in one step.
    :param oracle_batch_separator: The "batch separator" which will
     be placed between each statement when generating offline
     Oracle migrations.  Defaults to ``/``.  Oracle doesn't add a
     semicolon between statements like most other backends.

    """

def execute(sql, execution_options=None):
    """Execute the given SQL using the current change context.

    The behavior of :meth:`.execute` is the same
    as that of :meth:`.Operations.execute`.  Please see that
    function's documentation for full detail including
    caveats and limitations.

    This function requires that a :class:`.MigrationContext` has
    first been made available via :meth:`.configure`.

    """

def get_bind():
    """Return the current 'bind'.

    In "online" mode, this is the
    :class:`sqlalchemy.engine.Connection` currently being used
    to emit SQL to the database.

    This function requires that a :class:`.MigrationContext`
    has first been made available via :meth:`.configure`.

    """

def get_context() -> "MigrationContext":
    """Return the current :class:`.MigrationContext` object.

    If :meth:`.EnvironmentContext.configure` has not been
    called yet, raises an exception.

    """

def get_head_revision() -> Union[str, Tuple[str, ...], None]:
    """Return the hex identifier of the 'head' script revision.

    If the script directory has multiple heads, this
    method raises a :class:`.CommandError`;
    :meth:`.EnvironmentContext.get_head_revisions` should be preferred.

    This function does not require that the :class:`.MigrationContext`
    has been configured.

    .. seealso:: :meth:`.EnvironmentContext.get_head_revisions`

    """

def get_head_revisions() -> Union[str, Tuple[str, ...], None]:
    """Return the hex identifier of the 'heads' script revision(s).

    This returns a tuple containing the version number of all
    heads in the script directory.

    This function does not require that the :class:`.MigrationContext`
    has been configured.

    """

def get_revision_argument() -> Union[str, Tuple[str, ...], None]:
    """Get the 'destination' revision argument.

    This is typically the argument passed to the
    ``upgrade`` or ``downgrade`` command.

    If it was specified as ``head``, the actual
    version number is returned; if specified
    as ``base``, ``None`` is returned.

    This function does not require that the :class:`.MigrationContext`
    has been configured.

    """

def get_starting_revision_argument() -> Union[str, Tuple[str, ...], None]:
    """Return the 'starting revision' argument,
    if the revision was passed using ``start:end``.

    This is only meaningful in "offline" mode.
    Returns ``None`` if no value is available
    or was configured.

    This function does not require that the :class:`.MigrationContext`
    has been configured.

    """

def get_tag_argument() -> Optional[str]:
    """Return the value passed for the ``--tag`` argument, if any.

    The ``--tag`` argument is not used directly by Alembic,
    but is available for custom ``env.py`` configurations that
    wish to use it; particularly for offline generation scripts
    that wish to generate tagged filenames.

    This function does not require that the :class:`.MigrationContext`
    has been configured.

    .. seealso::

        :meth:`.EnvironmentContext.get_x_argument` - a newer and more
        open ended system of extending ``env.py`` scripts via the command
        line.

    """

def get_x_argument(as_dictionary: bool = False):
    """Return the value(s) passed for the ``-x`` argument, if any.

    The ``-x`` argument is an open ended flag that allows any user-defined
    value or values to be passed on the command line, then available
    here for consumption by a custom ``env.py`` script.

    The return value is a list, returned directly from the ``argparse``
    structure.  If ``as_dictionary=True`` is passed, the ``x`` arguments
    are parsed using ``key=value`` format into a dictionary that is
    then returned.

    For example, to support passing a database URL on the command line,
    the standard ``env.py`` script can be modified like this::

        cmd_line_url = context.get_x_argument(
            as_dictionary=True).get('dbname')
        if cmd_line_url:
            engine = create_engine(cmd_line_url)
        else:
            engine = engine_from_config(
                    config.get_section(config.config_ini_section),
                    prefix='sqlalchemy.',
                    poolclass=pool.NullPool)

    This then takes effect by running the ``alembic`` script as::

        alembic -x dbname=postgresql://user:pass@host/dbname upgrade head

    This function does not require that the :class:`.MigrationContext`
    has been configured.

    .. seealso::

        :meth:`.EnvironmentContext.get_tag_argument`

        :attr:`.Config.cmd_opts`

    """

def is_offline_mode() -> bool:
    """Return True if the current migrations environment
    is running in "offline mode".

    This is ``True`` or ``False`` depending
    on the ``--sql`` flag passed.

    This function does not require that the :class:`.MigrationContext`
    has been configured.

    """

def is_transactional_ddl():
    """Return True if the context is configured to expect a
    transactional DDL capable backend.

    This defaults to the type of database in use, and
    can be overridden by the ``transactional_ddl`` argument
    to :meth:`.configure`

    This function requires that a :class:`.MigrationContext`
    has first been made available via :meth:`.configure`.

    """

def run_migrations(**kw) -> None:
    """Run migrations as determined by the current command line
    configuration
    as well as versioning information present (or not) in the current
    database connection (if one is present).

    The function accepts optional ``**kw`` arguments.   If these are
    passed, they are sent directly to the ``upgrade()`` and
    ``downgrade()``
    functions within each target revision file.   By modifying the
    ``script.py.mako`` file so that the ``upgrade()`` and ``downgrade()``
    functions accept arguments, parameters can be passed here so that
    contextual information, usually information to identify a particular
    database in use, can be passed from a custom ``env.py`` script
    to the migration functions.

    This function requires that a :class:`.MigrationContext` has
    first been made available via :meth:`.configure`.

    """

def static_output(text):
    """Emit text directly to the "offline" SQL stream.

    Typically this is for emitting comments that
    start with --.  The statement is not treated
    as a SQL execution, no ; or batch separator
    is added, etc.

    """
