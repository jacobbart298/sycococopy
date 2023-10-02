// Generated from c:\Users\User\OneDrive\Documenten\Open Universiteit\IB9902 Voorbereiden Afstuderen\sycococopy\antlrFiles\Pythonic.g4 by ANTLR 4.9.2
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class PythonicParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.9.2", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PROTOCOL=1, ROLES=2, TO=3, FROM=4, SEND=5, SEQUENCE=6, SHUFFLE=7, CHOICE=8, 
		REPEAT=9, LOOP=10, CLOSE=11, WORD=12, WS=13, NL=14, INDENT=15, DEDENT=16;
	public static final int
		RULE_specification = 0, RULE_protocol = 1, RULE_expression = 2, RULE_sequence = 3, 
		RULE_shuffle = 4, RULE_choice = 5, RULE_loop = 6, RULE_repeat = 7, RULE_send = 8, 
		RULE_close = 9, RULE_block = 10, RULE_roles = 11, RULE_roleblock = 12, 
		RULE_role = 13;
	private static String[] makeRuleNames() {
		return new String[] {
			"specification", "protocol", "expression", "sequence", "shuffle", "choice", 
			"loop", "repeat", "send", "close", "block", "roles", "roleblock", "role"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'protocol:'", "'roles:'", "'to'", "'from'", "'send'", "'sequence:'", 
			"'shuffle:'", "'choice:'", "'repeat'", "'loop'", "'close'"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROTOCOL", "ROLES", "TO", "FROM", "SEND", "SEQUENCE", "SHUFFLE", 
			"CHOICE", "REPEAT", "LOOP", "CLOSE", "WORD", "WS", "NL", "INDENT", "DEDENT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "Pythonic.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public PythonicParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class SpecificationContext extends ParserRuleContext {
		public RolesContext roles() {
			return getRuleContext(RolesContext.class,0);
		}
		public ProtocolContext protocol() {
			return getRuleContext(ProtocolContext.class,0);
		}
		public TerminalNode EOF() { return getToken(PythonicParser.EOF, 0); }
		public SpecificationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_specification; }
	}

	public final SpecificationContext specification() throws RecognitionException {
		SpecificationContext _localctx = new SpecificationContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_specification);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(28);
			roles();
			setState(29);
			protocol();
			setState(30);
			match(EOF);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ProtocolContext extends ParserRuleContext {
		public TerminalNode PROTOCOL() { return getToken(PythonicParser.PROTOCOL, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ProtocolContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_protocol; }
	}

	public final ProtocolContext protocol() throws RecognitionException {
		ProtocolContext _localctx = new ProtocolContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_protocol);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(32);
			match(PROTOCOL);
			setState(33);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExpressionContext extends ParserRuleContext {
		public SendContext send() {
			return getRuleContext(SendContext.class,0);
		}
		public SequenceContext sequence() {
			return getRuleContext(SequenceContext.class,0);
		}
		public ShuffleContext shuffle() {
			return getRuleContext(ShuffleContext.class,0);
		}
		public ChoiceContext choice() {
			return getRuleContext(ChoiceContext.class,0);
		}
		public CloseContext close() {
			return getRuleContext(CloseContext.class,0);
		}
		public LoopContext loop() {
			return getRuleContext(LoopContext.class,0);
		}
		public RepeatContext repeat() {
			return getRuleContext(RepeatContext.class,0);
		}
		public ExpressionContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expression; }
	}

	public final ExpressionContext expression() throws RecognitionException {
		ExpressionContext _localctx = new ExpressionContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_expression);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(42);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SEND:
				{
				setState(35);
				send();
				}
				break;
			case SEQUENCE:
				{
				setState(36);
				sequence();
				}
				break;
			case SHUFFLE:
				{
				setState(37);
				shuffle();
				}
				break;
			case CHOICE:
				{
				setState(38);
				choice();
				}
				break;
			case CLOSE:
				{
				setState(39);
				close();
				}
				break;
			case LOOP:
				{
				setState(40);
				loop();
				}
				break;
			case REPEAT:
				{
				setState(41);
				repeat();
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SequenceContext extends ParserRuleContext {
		public TerminalNode SEQUENCE() { return getToken(PythonicParser.SEQUENCE, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public SequenceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_sequence; }
	}

	public final SequenceContext sequence() throws RecognitionException {
		SequenceContext _localctx = new SequenceContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_sequence);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(44);
			match(SEQUENCE);
			setState(45);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ShuffleContext extends ParserRuleContext {
		public TerminalNode SHUFFLE() { return getToken(PythonicParser.SHUFFLE, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ShuffleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_shuffle; }
	}

	public final ShuffleContext shuffle() throws RecognitionException {
		ShuffleContext _localctx = new ShuffleContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_shuffle);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(47);
			match(SHUFFLE);
			setState(48);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ChoiceContext extends ParserRuleContext {
		public TerminalNode CHOICE() { return getToken(PythonicParser.CHOICE, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public ChoiceContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_choice; }
	}

	public final ChoiceContext choice() throws RecognitionException {
		ChoiceContext _localctx = new ChoiceContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_choice);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(50);
			match(CHOICE);
			setState(51);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class LoopContext extends ParserRuleContext {
		public TerminalNode LOOP() { return getToken(PythonicParser.LOOP, 0); }
		public TerminalNode WORD() { return getToken(PythonicParser.WORD, 0); }
		public BlockContext block() {
			return getRuleContext(BlockContext.class,0);
		}
		public LoopContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_loop; }
	}

	public final LoopContext loop() throws RecognitionException {
		LoopContext _localctx = new LoopContext(_ctx, getState());
		enterRule(_localctx, 12, RULE_loop);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(53);
			match(LOOP);
			setState(54);
			match(WORD);
			setState(55);
			block();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RepeatContext extends ParserRuleContext {
		public TerminalNode REPEAT() { return getToken(PythonicParser.REPEAT, 0); }
		public TerminalNode WORD() { return getToken(PythonicParser.WORD, 0); }
		public RepeatContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_repeat; }
	}

	public final RepeatContext repeat() throws RecognitionException {
		RepeatContext _localctx = new RepeatContext(_ctx, getState());
		enterRule(_localctx, 14, RULE_repeat);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(57);
			match(REPEAT);
			setState(58);
			match(WORD);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class SendContext extends ParserRuleContext {
		public TerminalNode SEND() { return getToken(PythonicParser.SEND, 0); }
		public List<TerminalNode> WORD() { return getTokens(PythonicParser.WORD); }
		public TerminalNode WORD(int i) {
			return getToken(PythonicParser.WORD, i);
		}
		public TerminalNode FROM() { return getToken(PythonicParser.FROM, 0); }
		public TerminalNode TO() { return getToken(PythonicParser.TO, 0); }
		public TerminalNode NL() { return getToken(PythonicParser.NL, 0); }
		public SendContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_send; }
	}

	public final SendContext send() throws RecognitionException {
		SendContext _localctx = new SendContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_send);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(60);
			match(SEND);
			setState(61);
			match(WORD);
			setState(62);
			match(FROM);
			setState(63);
			match(WORD);
			setState(64);
			match(TO);
			setState(65);
			match(WORD);
			setState(66);
			match(NL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class CloseContext extends ParserRuleContext {
		public TerminalNode CLOSE() { return getToken(PythonicParser.CLOSE, 0); }
		public List<TerminalNode> WORD() { return getTokens(PythonicParser.WORD); }
		public TerminalNode WORD(int i) {
			return getToken(PythonicParser.WORD, i);
		}
		public TerminalNode TO() { return getToken(PythonicParser.TO, 0); }
		public TerminalNode NL() { return getToken(PythonicParser.NL, 0); }
		public CloseContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_close; }
	}

	public final CloseContext close() throws RecognitionException {
		CloseContext _localctx = new CloseContext(_ctx, getState());
		enterRule(_localctx, 18, RULE_close);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(68);
			match(CLOSE);
			setState(69);
			match(WORD);
			setState(70);
			match(TO);
			setState(71);
			match(WORD);
			setState(72);
			match(NL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class BlockContext extends ParserRuleContext {
		public TerminalNode INDENT() { return getToken(PythonicParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(PythonicParser.DEDENT, 0); }
		public List<ExpressionContext> expression() {
			return getRuleContexts(ExpressionContext.class);
		}
		public ExpressionContext expression(int i) {
			return getRuleContext(ExpressionContext.class,i);
		}
		public BlockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_block; }
	}

	public final BlockContext block() throws RecognitionException {
		BlockContext _localctx = new BlockContext(_ctx, getState());
		enterRule(_localctx, 20, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(74);
			match(INDENT);
			setState(76); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(75);
				expression();
				}
				}
				setState(78); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << SEND) | (1L << SEQUENCE) | (1L << SHUFFLE) | (1L << CHOICE) | (1L << REPEAT) | (1L << LOOP) | (1L << CLOSE))) != 0) );
			setState(80);
			match(DEDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RolesContext extends ParserRuleContext {
		public TerminalNode ROLES() { return getToken(PythonicParser.ROLES, 0); }
		public RoleblockContext roleblock() {
			return getRuleContext(RoleblockContext.class,0);
		}
		public RolesContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_roles; }
	}

	public final RolesContext roles() throws RecognitionException {
		RolesContext _localctx = new RolesContext(_ctx, getState());
		enterRule(_localctx, 22, RULE_roles);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(82);
			match(ROLES);
			setState(83);
			roleblock();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RoleblockContext extends ParserRuleContext {
		public TerminalNode INDENT() { return getToken(PythonicParser.INDENT, 0); }
		public TerminalNode DEDENT() { return getToken(PythonicParser.DEDENT, 0); }
		public List<RoleContext> role() {
			return getRuleContexts(RoleContext.class);
		}
		public RoleContext role(int i) {
			return getRuleContext(RoleContext.class,i);
		}
		public RoleblockContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_roleblock; }
	}

	public final RoleblockContext roleblock() throws RecognitionException {
		RoleblockContext _localctx = new RoleblockContext(_ctx, getState());
		enterRule(_localctx, 24, RULE_roleblock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(85);
			match(INDENT);
			setState(87); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(86);
				role();
				}
				}
				setState(89); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==WORD );
			setState(91);
			match(DEDENT);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class RoleContext extends ParserRuleContext {
		public TerminalNode WORD() { return getToken(PythonicParser.WORD, 0); }
		public TerminalNode NL() { return getToken(PythonicParser.NL, 0); }
		public RoleContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_role; }
	}

	public final RoleContext role() throws RecognitionException {
		RoleContext _localctx = new RoleContext(_ctx, getState());
		enterRule(_localctx, 26, RULE_role);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(93);
			match(WORD);
			setState(94);
			match(NL);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static final String _serializedATN =
		"\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22c\4\2\t\2\4\3\t"+
		"\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4"+
		"\f\t\f\4\r\t\r\4\16\t\16\4\17\t\17\3\2\3\2\3\2\3\2\3\3\3\3\3\3\3\4\3\4"+
		"\3\4\3\4\3\4\3\4\3\4\5\4-\n\4\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b"+
		"\3\b\3\b\3\b\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3\13"+
		"\3\13\3\13\3\13\3\f\3\f\6\fO\n\f\r\f\16\fP\3\f\3\f\3\r\3\r\3\r\3\16\3"+
		"\16\6\16Z\n\16\r\16\16\16[\3\16\3\16\3\17\3\17\3\17\3\17\2\2\20\2\4\6"+
		"\b\n\f\16\20\22\24\26\30\32\34\2\2\2\\\2\36\3\2\2\2\4\"\3\2\2\2\6,\3\2"+
		"\2\2\b.\3\2\2\2\n\61\3\2\2\2\f\64\3\2\2\2\16\67\3\2\2\2\20;\3\2\2\2\22"+
		">\3\2\2\2\24F\3\2\2\2\26L\3\2\2\2\30T\3\2\2\2\32W\3\2\2\2\34_\3\2\2\2"+
		"\36\37\5\30\r\2\37 \5\4\3\2 !\7\2\2\3!\3\3\2\2\2\"#\7\3\2\2#$\5\26\f\2"+
		"$\5\3\2\2\2%-\5\22\n\2&-\5\b\5\2\'-\5\n\6\2(-\5\f\7\2)-\5\24\13\2*-\5"+
		"\16\b\2+-\5\20\t\2,%\3\2\2\2,&\3\2\2\2,\'\3\2\2\2,(\3\2\2\2,)\3\2\2\2"+
		",*\3\2\2\2,+\3\2\2\2-\7\3\2\2\2./\7\b\2\2/\60\5\26\f\2\60\t\3\2\2\2\61"+
		"\62\7\t\2\2\62\63\5\26\f\2\63\13\3\2\2\2\64\65\7\n\2\2\65\66\5\26\f\2"+
		"\66\r\3\2\2\2\678\7\f\2\289\7\16\2\29:\5\26\f\2:\17\3\2\2\2;<\7\13\2\2"+
		"<=\7\16\2\2=\21\3\2\2\2>?\7\7\2\2?@\7\16\2\2@A\7\6\2\2AB\7\16\2\2BC\7"+
		"\5\2\2CD\7\16\2\2DE\7\20\2\2E\23\3\2\2\2FG\7\r\2\2GH\7\16\2\2HI\7\5\2"+
		"\2IJ\7\16\2\2JK\7\20\2\2K\25\3\2\2\2LN\7\21\2\2MO\5\6\4\2NM\3\2\2\2OP"+
		"\3\2\2\2PN\3\2\2\2PQ\3\2\2\2QR\3\2\2\2RS\7\22\2\2S\27\3\2\2\2TU\7\4\2"+
		"\2UV\5\32\16\2V\31\3\2\2\2WY\7\21\2\2XZ\5\34\17\2YX\3\2\2\2Z[\3\2\2\2"+
		"[Y\3\2\2\2[\\\3\2\2\2\\]\3\2\2\2]^\7\22\2\2^\33\3\2\2\2_`\7\16\2\2`a\7"+
		"\20\2\2a\35\3\2\2\2\5,P[";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}