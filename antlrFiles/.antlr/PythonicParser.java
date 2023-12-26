// Generated from c:/Users/User/OneDrive/Documenten/Open Universiteit/IB9902 Voorbereiden Afstuderen/sycococopy/antlrFiles/Pythonic.g4 by ANTLR 4.13.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast", "CheckReturnValue"})
public class PythonicParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.13.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		PROTOCOL=1, ROLES=2, TO=3, FROM=4, SEND=5, SEQUENCE=6, SHUFFLE=7, CHOICE=8, 
		REPEAT=9, LOOP=10, LOOPLABEL=11, OPENINGBRACKET=12, CLOSINGBRACKET=13, 
		COMMA=14, BOOLEAN=15, PRIMITIVE=16, INTEGER=17, STRING=18, FLOAT=19, COMPARATOR=20, 
		WORD=21, WS=22, NL=23, INDENT=24, DEDENT=25;
	public static final int
		RULE_specification = 0, RULE_protocol = 1, RULE_expression = 2, RULE_sequence = 3, 
		RULE_shuffle = 4, RULE_choice = 5, RULE_loop = 6, RULE_repeat = 7, RULE_send = 8, 
		RULE_block = 9, RULE_roles = 10, RULE_roleblock = 11, RULE_role = 12;
	private static String[] makeRuleNames() {
		return new String[] {
			"specification", "protocol", "expression", "sequence", "shuffle", "choice", 
			"loop", "repeat", "send", "block", "roles", "roleblock", "role"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "'protocol:'", "'roles:'", "'to'", "'from'", "'send'", "'sequence:'", 
			"'shuffle:'", "'choice:'", "'repeat'", "'loop'", null, "'('", "')'", 
			"','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROTOCOL", "ROLES", "TO", "FROM", "SEND", "SEQUENCE", "SHUFFLE", 
			"CHOICE", "REPEAT", "LOOP", "LOOPLABEL", "OPENINGBRACKET", "CLOSINGBRACKET", 
			"COMMA", "BOOLEAN", "PRIMITIVE", "INTEGER", "STRING", "FLOAT", "COMPARATOR", 
			"WORD", "WS", "NL", "INDENT", "DEDENT"
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

	@SuppressWarnings("CheckReturnValue")
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
			setState(26);
			roles();
			setState(27);
			protocol();
			setState(28);
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

	@SuppressWarnings("CheckReturnValue")
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
			setState(30);
			match(PROTOCOL);
			setState(31);
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

	@SuppressWarnings("CheckReturnValue")
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
			setState(39);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case SEND:
				{
				setState(33);
				send();
				}
				break;
			case SEQUENCE:
				{
				setState(34);
				sequence();
				}
				break;
			case SHUFFLE:
				{
				setState(35);
				shuffle();
				}
				break;
			case CHOICE:
				{
				setState(36);
				choice();
				}
				break;
			case LOOP:
				{
				setState(37);
				loop();
				}
				break;
			case REPEAT:
				{
				setState(38);
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

	@SuppressWarnings("CheckReturnValue")
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
			setState(41);
			match(SEQUENCE);
			setState(42);
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

	@SuppressWarnings("CheckReturnValue")
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
			setState(44);
			match(SHUFFLE);
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

	@SuppressWarnings("CheckReturnValue")
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
			setState(47);
			match(CHOICE);
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

	@SuppressWarnings("CheckReturnValue")
	public static class LoopContext extends ParserRuleContext {
		public TerminalNode LOOP() { return getToken(PythonicParser.LOOP, 0); }
		public TerminalNode LOOPLABEL() { return getToken(PythonicParser.LOOPLABEL, 0); }
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
			setState(50);
			match(LOOP);
			setState(51);
			match(LOOPLABEL);
			setState(52);
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

	@SuppressWarnings("CheckReturnValue")
	public static class RepeatContext extends ParserRuleContext {
		public TerminalNode REPEAT() { return getToken(PythonicParser.REPEAT, 0); }
		public TerminalNode WORD() { return getToken(PythonicParser.WORD, 0); }
		public TerminalNode NL() { return getToken(PythonicParser.NL, 0); }
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
			setState(54);
			match(REPEAT);
			setState(55);
			match(WORD);
			setState(56);
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

	@SuppressWarnings("CheckReturnValue")
	public static class SendContext extends ParserRuleContext {
		public TerminalNode SEND() { return getToken(PythonicParser.SEND, 0); }
		public List<TerminalNode> WORD() { return getTokens(PythonicParser.WORD); }
		public TerminalNode WORD(int i) {
			return getToken(PythonicParser.WORD, i);
		}
		public TerminalNode FROM() { return getToken(PythonicParser.FROM, 0); }
		public TerminalNode TO() { return getToken(PythonicParser.TO, 0); }
		public TerminalNode NL() { return getToken(PythonicParser.NL, 0); }
		public List<TerminalNode> OPENINGBRACKET() { return getTokens(PythonicParser.OPENINGBRACKET); }
		public TerminalNode OPENINGBRACKET(int i) {
			return getToken(PythonicParser.OPENINGBRACKET, i);
		}
		public TerminalNode COMPARATOR() { return getToken(PythonicParser.COMPARATOR, 0); }
		public List<TerminalNode> CLOSINGBRACKET() { return getTokens(PythonicParser.CLOSINGBRACKET); }
		public TerminalNode CLOSINGBRACKET(int i) {
			return getToken(PythonicParser.CLOSINGBRACKET, i);
		}
		public List<TerminalNode> PRIMITIVE() { return getTokens(PythonicParser.PRIMITIVE); }
		public TerminalNode PRIMITIVE(int i) {
			return getToken(PythonicParser.PRIMITIVE, i);
		}
		public List<TerminalNode> BOOLEAN() { return getTokens(PythonicParser.BOOLEAN); }
		public TerminalNode BOOLEAN(int i) {
			return getToken(PythonicParser.BOOLEAN, i);
		}
		public List<TerminalNode> COMMA() { return getTokens(PythonicParser.COMMA); }
		public TerminalNode COMMA(int i) {
			return getToken(PythonicParser.COMMA, i);
		}
		public SendContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_send; }
	}

	public final SendContext send() throws RecognitionException {
		SendContext _localctx = new SendContext(_ctx, getState());
		enterRule(_localctx, 16, RULE_send);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(119);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				{
				setState(58);
				match(SEND);
				setState(59);
				match(WORD);
				setState(60);
				match(FROM);
				setState(61);
				match(WORD);
				setState(62);
				match(TO);
				setState(63);
				match(WORD);
				setState(64);
				match(NL);
				}
				}
				break;
			case 2:
				{
				{
				setState(65);
				match(SEND);
				setState(66);
				match(WORD);
				setState(67);
				match(OPENINGBRACKET);
				setState(68);
				match(COMPARATOR);
				setState(84);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case PRIMITIVE:
					{
					setState(69);
					match(PRIMITIVE);
					}
					break;
				case WORD:
					{
					{
					setState(70);
					match(WORD);
					setState(71);
					match(OPENINGBRACKET);
					setState(81);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case BOOLEAN:
					case PRIMITIVE:
						{
						{
						setState(72);
						_la = _input.LA(1);
						if ( !(_la==BOOLEAN || _la==PRIMITIVE) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(77);
						_errHandler.sync(this);
						_la = _input.LA(1);
						while (_la==COMMA) {
							{
							{
							setState(73);
							match(COMMA);
							setState(74);
							_la = _input.LA(1);
							if ( !(_la==BOOLEAN || _la==PRIMITIVE) ) {
							_errHandler.recoverInline(this);
							}
							else {
								if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
								_errHandler.reportMatch(this);
								consume();
							}
							}
							}
							setState(79);
							_errHandler.sync(this);
							_la = _input.LA(1);
						}
						}
						}
						break;
					case CLOSINGBRACKET:
						{
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(83);
					match(CLOSINGBRACKET);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(86);
				match(CLOSINGBRACKET);
				setState(87);
				match(FROM);
				setState(88);
				match(WORD);
				setState(89);
				match(TO);
				setState(90);
				match(WORD);
				setState(91);
				match(NL);
				}
				}
				break;
			case 3:
				{
				{
				setState(92);
				match(SEND);
				setState(93);
				match(WORD);
				setState(94);
				match(OPENINGBRACKET);
				setState(111);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case BOOLEAN:
					{
					setState(95);
					match(BOOLEAN);
					}
					break;
				case PRIMITIVE:
					{
					setState(96);
					match(PRIMITIVE);
					}
					break;
				case WORD:
					{
					{
					setState(97);
					match(WORD);
					setState(98);
					match(OPENINGBRACKET);
					setState(108);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case BOOLEAN:
					case PRIMITIVE:
						{
						{
						setState(99);
						_la = _input.LA(1);
						if ( !(_la==BOOLEAN || _la==PRIMITIVE) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(104);
						_errHandler.sync(this);
						_la = _input.LA(1);
						while (_la==COMMA) {
							{
							{
							setState(100);
							match(COMMA);
							setState(101);
							_la = _input.LA(1);
							if ( !(_la==BOOLEAN || _la==PRIMITIVE) ) {
							_errHandler.recoverInline(this);
							}
							else {
								if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
								_errHandler.reportMatch(this);
								consume();
							}
							}
							}
							setState(106);
							_errHandler.sync(this);
							_la = _input.LA(1);
						}
						}
						}
						break;
					case CLOSINGBRACKET:
						{
						}
						break;
					default:
						throw new NoViableAltException(this);
					}
					setState(110);
					match(CLOSINGBRACKET);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(113);
				match(CLOSINGBRACKET);
				setState(114);
				match(FROM);
				setState(115);
				match(WORD);
				setState(116);
				match(TO);
				setState(117);
				match(WORD);
				setState(118);
				match(NL);
				}
				}
				break;
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

	@SuppressWarnings("CheckReturnValue")
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
		enterRule(_localctx, 18, RULE_block);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(121);
			match(INDENT);
			setState(123); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(122);
				expression();
				}
				}
				setState(125); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 2016L) != 0) );
			setState(127);
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

	@SuppressWarnings("CheckReturnValue")
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
		enterRule(_localctx, 20, RULE_roles);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(129);
			match(ROLES);
			setState(130);
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

	@SuppressWarnings("CheckReturnValue")
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
		enterRule(_localctx, 22, RULE_roleblock);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(132);
			match(INDENT);
			setState(134); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(133);
				role();
				}
				}
				setState(136); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==WORD );
			setState(138);
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

	@SuppressWarnings("CheckReturnValue")
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
		enterRule(_localctx, 24, RULE_role);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(140);
			match(WORD);
			setState(141);
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
		"\u0004\u0001\u0019\u0090\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0001\u0000\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0003\u0002(\b\u0002\u0001\u0003\u0001"+
		"\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001\u0004\u0001\u0005\u0001"+
		"\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0005\bL\b\b\n\b\f\bO\t\b\u0001\b\u0003"+
		"\bR\b\b\u0001\b\u0003\bU\b\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0005\bg\b\b\n\b\f\bj\t\b\u0001\b\u0003\bm\b\b\u0001\b\u0003"+
		"\bp\b\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0003\bx\b\b\u0001"+
		"\t\u0001\t\u0004\t|\b\t\u000b\t\f\t}\u0001\t\u0001\t\u0001\n\u0001\n\u0001"+
		"\n\u0001\u000b\u0001\u000b\u0004\u000b\u0087\b\u000b\u000b\u000b\f\u000b"+
		"\u0088\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0001\f\u0000\u0000"+
		"\r\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014\u0016\u0018\u0000"+
		"\u0001\u0001\u0000\u000f\u0010\u0092\u0000\u001a\u0001\u0000\u0000\u0000"+
		"\u0002\u001e\u0001\u0000\u0000\u0000\u0004\'\u0001\u0000\u0000\u0000\u0006"+
		")\u0001\u0000\u0000\u0000\b,\u0001\u0000\u0000\u0000\n/\u0001\u0000\u0000"+
		"\u0000\f2\u0001\u0000\u0000\u0000\u000e6\u0001\u0000\u0000\u0000\u0010"+
		"w\u0001\u0000\u0000\u0000\u0012y\u0001\u0000\u0000\u0000\u0014\u0081\u0001"+
		"\u0000\u0000\u0000\u0016\u0084\u0001\u0000\u0000\u0000\u0018\u008c\u0001"+
		"\u0000\u0000\u0000\u001a\u001b\u0003\u0014\n\u0000\u001b\u001c\u0003\u0002"+
		"\u0001\u0000\u001c\u001d\u0005\u0000\u0000\u0001\u001d\u0001\u0001\u0000"+
		"\u0000\u0000\u001e\u001f\u0005\u0001\u0000\u0000\u001f \u0003\u0012\t"+
		"\u0000 \u0003\u0001\u0000\u0000\u0000!(\u0003\u0010\b\u0000\"(\u0003\u0006"+
		"\u0003\u0000#(\u0003\b\u0004\u0000$(\u0003\n\u0005\u0000%(\u0003\f\u0006"+
		"\u0000&(\u0003\u000e\u0007\u0000\'!\u0001\u0000\u0000\u0000\'\"\u0001"+
		"\u0000\u0000\u0000\'#\u0001\u0000\u0000\u0000\'$\u0001\u0000\u0000\u0000"+
		"\'%\u0001\u0000\u0000\u0000\'&\u0001\u0000\u0000\u0000(\u0005\u0001\u0000"+
		"\u0000\u0000)*\u0005\u0006\u0000\u0000*+\u0003\u0012\t\u0000+\u0007\u0001"+
		"\u0000\u0000\u0000,-\u0005\u0007\u0000\u0000-.\u0003\u0012\t\u0000.\t"+
		"\u0001\u0000\u0000\u0000/0\u0005\b\u0000\u000001\u0003\u0012\t\u00001"+
		"\u000b\u0001\u0000\u0000\u000023\u0005\n\u0000\u000034\u0005\u000b\u0000"+
		"\u000045\u0003\u0012\t\u00005\r\u0001\u0000\u0000\u000067\u0005\t\u0000"+
		"\u000078\u0005\u0015\u0000\u000089\u0005\u0017\u0000\u00009\u000f\u0001"+
		"\u0000\u0000\u0000:;\u0005\u0005\u0000\u0000;<\u0005\u0015\u0000\u0000"+
		"<=\u0005\u0004\u0000\u0000=>\u0005\u0015\u0000\u0000>?\u0005\u0003\u0000"+
		"\u0000?@\u0005\u0015\u0000\u0000@x\u0005\u0017\u0000\u0000AB\u0005\u0005"+
		"\u0000\u0000BC\u0005\u0015\u0000\u0000CD\u0005\f\u0000\u0000DT\u0005\u0014"+
		"\u0000\u0000EU\u0005\u0010\u0000\u0000FG\u0005\u0015\u0000\u0000GQ\u0005"+
		"\f\u0000\u0000HM\u0007\u0000\u0000\u0000IJ\u0005\u000e\u0000\u0000JL\u0007"+
		"\u0000\u0000\u0000KI\u0001\u0000\u0000\u0000LO\u0001\u0000\u0000\u0000"+
		"MK\u0001\u0000\u0000\u0000MN\u0001\u0000\u0000\u0000NR\u0001\u0000\u0000"+
		"\u0000OM\u0001\u0000\u0000\u0000PR\u0001\u0000\u0000\u0000QH\u0001\u0000"+
		"\u0000\u0000QP\u0001\u0000\u0000\u0000RS\u0001\u0000\u0000\u0000SU\u0005"+
		"\r\u0000\u0000TE\u0001\u0000\u0000\u0000TF\u0001\u0000\u0000\u0000UV\u0001"+
		"\u0000\u0000\u0000VW\u0005\r\u0000\u0000WX\u0005\u0004\u0000\u0000XY\u0005"+
		"\u0015\u0000\u0000YZ\u0005\u0003\u0000\u0000Z[\u0005\u0015\u0000\u0000"+
		"[x\u0005\u0017\u0000\u0000\\]\u0005\u0005\u0000\u0000]^\u0005\u0015\u0000"+
		"\u0000^o\u0005\f\u0000\u0000_p\u0005\u000f\u0000\u0000`p\u0005\u0010\u0000"+
		"\u0000ab\u0005\u0015\u0000\u0000bl\u0005\f\u0000\u0000ch\u0007\u0000\u0000"+
		"\u0000de\u0005\u000e\u0000\u0000eg\u0007\u0000\u0000\u0000fd\u0001\u0000"+
		"\u0000\u0000gj\u0001\u0000\u0000\u0000hf\u0001\u0000\u0000\u0000hi\u0001"+
		"\u0000\u0000\u0000im\u0001\u0000\u0000\u0000jh\u0001\u0000\u0000\u0000"+
		"km\u0001\u0000\u0000\u0000lc\u0001\u0000\u0000\u0000lk\u0001\u0000\u0000"+
		"\u0000mn\u0001\u0000\u0000\u0000np\u0005\r\u0000\u0000o_\u0001\u0000\u0000"+
		"\u0000o`\u0001\u0000\u0000\u0000oa\u0001\u0000\u0000\u0000pq\u0001\u0000"+
		"\u0000\u0000qr\u0005\r\u0000\u0000rs\u0005\u0004\u0000\u0000st\u0005\u0015"+
		"\u0000\u0000tu\u0005\u0003\u0000\u0000uv\u0005\u0015\u0000\u0000vx\u0005"+
		"\u0017\u0000\u0000w:\u0001\u0000\u0000\u0000wA\u0001\u0000\u0000\u0000"+
		"w\\\u0001\u0000\u0000\u0000x\u0011\u0001\u0000\u0000\u0000y{\u0005\u0018"+
		"\u0000\u0000z|\u0003\u0004\u0002\u0000{z\u0001\u0000\u0000\u0000|}\u0001"+
		"\u0000\u0000\u0000}{\u0001\u0000\u0000\u0000}~\u0001\u0000\u0000\u0000"+
		"~\u007f\u0001\u0000\u0000\u0000\u007f\u0080\u0005\u0019\u0000\u0000\u0080"+
		"\u0013\u0001\u0000\u0000\u0000\u0081\u0082\u0005\u0002\u0000\u0000\u0082"+
		"\u0083\u0003\u0016\u000b\u0000\u0083\u0015\u0001\u0000\u0000\u0000\u0084"+
		"\u0086\u0005\u0018\u0000\u0000\u0085\u0087\u0003\u0018\f\u0000\u0086\u0085"+
		"\u0001\u0000\u0000\u0000\u0087\u0088\u0001\u0000\u0000\u0000\u0088\u0086"+
		"\u0001\u0000\u0000\u0000\u0088\u0089\u0001\u0000\u0000\u0000\u0089\u008a"+
		"\u0001\u0000\u0000\u0000\u008a\u008b\u0005\u0019\u0000\u0000\u008b\u0017"+
		"\u0001\u0000\u0000\u0000\u008c\u008d\u0005\u0015\u0000\u0000\u008d\u008e"+
		"\u0005\u0017\u0000\u0000\u008e\u0019\u0001\u0000\u0000\u0000\n\'MQThl"+
		"ow}\u0088";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}