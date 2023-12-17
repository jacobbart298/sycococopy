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
		REPEAT=9, LOOP=10, CLOSE=11, LOOPLABEL=12, OPENINGBRACKET=13, CLOSINGBRACKET=14, 
		COMMA=15, BOOLEAN=16, PRIMITIVE=17, INTEGER=18, STRING=19, FLOAT=20, COMPARATOR=21, 
		WORD=22, WS=23, NL=24, INDENT=25, DEDENT=26;
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
			"'shuffle:'", "'choice:'", "'repeat'", "'loop'", "'close'", null, "'('", 
			"')'", "','"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, "PROTOCOL", "ROLES", "TO", "FROM", "SEND", "SEQUENCE", "SHUFFLE", 
			"CHOICE", "REPEAT", "LOOP", "CLOSE", "LOOPLABEL", "OPENINGBRACKET", "CLOSINGBRACKET", 
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
			setState(53);
			match(LOOP);
			setState(54);
			match(LOOPLABEL);
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
			setState(57);
			match(REPEAT);
			setState(58);
			match(WORD);
			setState(59);
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
			setState(122);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,7,_ctx) ) {
			case 1:
				{
				{
				setState(61);
				match(SEND);
				setState(62);
				match(WORD);
				setState(63);
				match(FROM);
				setState(64);
				match(WORD);
				setState(65);
				match(TO);
				setState(66);
				match(WORD);
				setState(67);
				match(NL);
				}
				}
				break;
			case 2:
				{
				{
				setState(68);
				match(SEND);
				setState(69);
				match(WORD);
				setState(70);
				match(OPENINGBRACKET);
				setState(71);
				match(COMPARATOR);
				setState(87);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case PRIMITIVE:
					{
					setState(72);
					match(PRIMITIVE);
					}
					break;
				case WORD:
					{
					{
					setState(73);
					match(WORD);
					setState(74);
					match(OPENINGBRACKET);
					setState(84);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case BOOLEAN:
					case PRIMITIVE:
						{
						{
						setState(75);
						_la = _input.LA(1);
						if ( !(_la==BOOLEAN || _la==PRIMITIVE) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(80);
						_errHandler.sync(this);
						_la = _input.LA(1);
						while (_la==COMMA) {
							{
							{
							setState(76);
							match(COMMA);
							setState(77);
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
							setState(82);
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
					setState(86);
					match(CLOSINGBRACKET);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(89);
				match(CLOSINGBRACKET);
				setState(90);
				match(FROM);
				setState(91);
				match(WORD);
				setState(92);
				match(TO);
				setState(93);
				match(WORD);
				setState(94);
				match(NL);
				}
				}
				break;
			case 3:
				{
				{
				setState(95);
				match(SEND);
				setState(96);
				match(WORD);
				setState(97);
				match(OPENINGBRACKET);
				setState(114);
				_errHandler.sync(this);
				switch (_input.LA(1)) {
				case BOOLEAN:
					{
					setState(98);
					match(BOOLEAN);
					}
					break;
				case PRIMITIVE:
					{
					setState(99);
					match(PRIMITIVE);
					}
					break;
				case WORD:
					{
					{
					setState(100);
					match(WORD);
					setState(101);
					match(OPENINGBRACKET);
					setState(111);
					_errHandler.sync(this);
					switch (_input.LA(1)) {
					case BOOLEAN:
					case PRIMITIVE:
						{
						{
						setState(102);
						_la = _input.LA(1);
						if ( !(_la==BOOLEAN || _la==PRIMITIVE) ) {
						_errHandler.recoverInline(this);
						}
						else {
							if ( _input.LA(1)==Token.EOF ) matchedEOF = true;
							_errHandler.reportMatch(this);
							consume();
						}
						setState(107);
						_errHandler.sync(this);
						_la = _input.LA(1);
						while (_la==COMMA) {
							{
							{
							setState(103);
							match(COMMA);
							setState(104);
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
							setState(109);
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
					setState(113);
					match(CLOSINGBRACKET);
					}
					}
					break;
				default:
					throw new NoViableAltException(this);
				}
				setState(116);
				match(CLOSINGBRACKET);
				setState(117);
				match(FROM);
				setState(118);
				match(WORD);
				setState(119);
				match(TO);
				setState(120);
				match(WORD);
				setState(121);
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
			setState(124);
			match(CLOSE);
			setState(125);
			match(WORD);
			setState(126);
			match(TO);
			setState(127);
			match(WORD);
			setState(128);
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
			setState(130);
			match(INDENT);
			setState(132); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(131);
				expression();
				}
				}
				setState(134); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & 4064L) != 0) );
			setState(136);
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
		enterRule(_localctx, 22, RULE_roles);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(138);
			match(ROLES);
			setState(139);
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
		public List<RoleContext> role() {
			return getRuleContexts(RoleContext.class);
		}
		public RoleContext role(int i) {
			return getRuleContext(RoleContext.class,i);
		}
		public TerminalNode DEDENT() { return getToken(PythonicParser.DEDENT, 0); }
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
			setState(141);
			match(INDENT);
			setState(142);
			role();
			setState(144); 
			_errHandler.sync(this);
			_la = _input.LA(1);
			do {
				{
				{
				setState(143);
				role();
				}
				}
				setState(146); 
				_errHandler.sync(this);
				_la = _input.LA(1);
			} while ( _la==WORD );
			setState(148);
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
		enterRule(_localctx, 26, RULE_role);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(150);
			match(WORD);
			setState(151);
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
		"\u0004\u0001\u001a\u009a\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001"+
		"\u0002\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004"+
		"\u0002\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0002\u0007\u0007\u0007"+
		"\u0002\b\u0007\b\u0002\t\u0007\t\u0002\n\u0007\n\u0002\u000b\u0007\u000b"+
		"\u0002\f\u0007\f\u0002\r\u0007\r\u0001\u0000\u0001\u0000\u0001\u0000\u0001"+
		"\u0000\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0002\u0001\u0002\u0001"+
		"\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002+\b"+
		"\u0002\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0007\u0001\u0007\u0001\u0007\u0001\u0007\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0005\bO\b"+
		"\b\n\b\f\bR\t\b\u0001\b\u0003\bU\b\b\u0001\b\u0003\bX\b\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001\b\u0005\bj\b\b\n\b\f\bm\t\b\u0001"+
		"\b\u0003\bp\b\b\u0001\b\u0003\bs\b\b\u0001\b\u0001\b\u0001\b\u0001\b\u0001"+
		"\b\u0001\b\u0003\b{\b\b\u0001\t\u0001\t\u0001\t\u0001\t\u0001\t\u0001"+
		"\t\u0001\n\u0001\n\u0004\n\u0085\b\n\u000b\n\f\n\u0086\u0001\n\u0001\n"+
		"\u0001\u000b\u0001\u000b\u0001\u000b\u0001\f\u0001\f\u0001\f\u0004\f\u0091"+
		"\b\f\u000b\f\f\f\u0092\u0001\f\u0001\f\u0001\r\u0001\r\u0001\r\u0001\r"+
		"\u0000\u0000\u000e\u0000\u0002\u0004\u0006\b\n\f\u000e\u0010\u0012\u0014"+
		"\u0016\u0018\u001a\u0000\u0001\u0001\u0000\u0010\u0011\u009c\u0000\u001c"+
		"\u0001\u0000\u0000\u0000\u0002 \u0001\u0000\u0000\u0000\u0004*\u0001\u0000"+
		"\u0000\u0000\u0006,\u0001\u0000\u0000\u0000\b/\u0001\u0000\u0000\u0000"+
		"\n2\u0001\u0000\u0000\u0000\f5\u0001\u0000\u0000\u0000\u000e9\u0001\u0000"+
		"\u0000\u0000\u0010z\u0001\u0000\u0000\u0000\u0012|\u0001\u0000\u0000\u0000"+
		"\u0014\u0082\u0001\u0000\u0000\u0000\u0016\u008a\u0001\u0000\u0000\u0000"+
		"\u0018\u008d\u0001\u0000\u0000\u0000\u001a\u0096\u0001\u0000\u0000\u0000"+
		"\u001c\u001d\u0003\u0016\u000b\u0000\u001d\u001e\u0003\u0002\u0001\u0000"+
		"\u001e\u001f\u0005\u0000\u0000\u0001\u001f\u0001\u0001\u0000\u0000\u0000"+
		" !\u0005\u0001\u0000\u0000!\"\u0003\u0014\n\u0000\"\u0003\u0001\u0000"+
		"\u0000\u0000#+\u0003\u0010\b\u0000$+\u0003\u0006\u0003\u0000%+\u0003\b"+
		"\u0004\u0000&+\u0003\n\u0005\u0000\'+\u0003\u0012\t\u0000(+\u0003\f\u0006"+
		"\u0000)+\u0003\u000e\u0007\u0000*#\u0001\u0000\u0000\u0000*$\u0001\u0000"+
		"\u0000\u0000*%\u0001\u0000\u0000\u0000*&\u0001\u0000\u0000\u0000*\'\u0001"+
		"\u0000\u0000\u0000*(\u0001\u0000\u0000\u0000*)\u0001\u0000\u0000\u0000"+
		"+\u0005\u0001\u0000\u0000\u0000,-\u0005\u0006\u0000\u0000-.\u0003\u0014"+
		"\n\u0000.\u0007\u0001\u0000\u0000\u0000/0\u0005\u0007\u0000\u000001\u0003"+
		"\u0014\n\u00001\t\u0001\u0000\u0000\u000023\u0005\b\u0000\u000034\u0003"+
		"\u0014\n\u00004\u000b\u0001\u0000\u0000\u000056\u0005\n\u0000\u000067"+
		"\u0005\f\u0000\u000078\u0003\u0014\n\u00008\r\u0001\u0000\u0000\u0000"+
		"9:\u0005\t\u0000\u0000:;\u0005\u0016\u0000\u0000;<\u0005\u0018\u0000\u0000"+
		"<\u000f\u0001\u0000\u0000\u0000=>\u0005\u0005\u0000\u0000>?\u0005\u0016"+
		"\u0000\u0000?@\u0005\u0004\u0000\u0000@A\u0005\u0016\u0000\u0000AB\u0005"+
		"\u0003\u0000\u0000BC\u0005\u0016\u0000\u0000C{\u0005\u0018\u0000\u0000"+
		"DE\u0005\u0005\u0000\u0000EF\u0005\u0016\u0000\u0000FG\u0005\r\u0000\u0000"+
		"GW\u0005\u0015\u0000\u0000HX\u0005\u0011\u0000\u0000IJ\u0005\u0016\u0000"+
		"\u0000JT\u0005\r\u0000\u0000KP\u0007\u0000\u0000\u0000LM\u0005\u000f\u0000"+
		"\u0000MO\u0007\u0000\u0000\u0000NL\u0001\u0000\u0000\u0000OR\u0001\u0000"+
		"\u0000\u0000PN\u0001\u0000\u0000\u0000PQ\u0001\u0000\u0000\u0000QU\u0001"+
		"\u0000\u0000\u0000RP\u0001\u0000\u0000\u0000SU\u0001\u0000\u0000\u0000"+
		"TK\u0001\u0000\u0000\u0000TS\u0001\u0000\u0000\u0000UV\u0001\u0000\u0000"+
		"\u0000VX\u0005\u000e\u0000\u0000WH\u0001\u0000\u0000\u0000WI\u0001\u0000"+
		"\u0000\u0000XY\u0001\u0000\u0000\u0000YZ\u0005\u000e\u0000\u0000Z[\u0005"+
		"\u0004\u0000\u0000[\\\u0005\u0016\u0000\u0000\\]\u0005\u0003\u0000\u0000"+
		"]^\u0005\u0016\u0000\u0000^{\u0005\u0018\u0000\u0000_`\u0005\u0005\u0000"+
		"\u0000`a\u0005\u0016\u0000\u0000ar\u0005\r\u0000\u0000bs\u0005\u0010\u0000"+
		"\u0000cs\u0005\u0011\u0000\u0000de\u0005\u0016\u0000\u0000eo\u0005\r\u0000"+
		"\u0000fk\u0007\u0000\u0000\u0000gh\u0005\u000f\u0000\u0000hj\u0007\u0000"+
		"\u0000\u0000ig\u0001\u0000\u0000\u0000jm\u0001\u0000\u0000\u0000ki\u0001"+
		"\u0000\u0000\u0000kl\u0001\u0000\u0000\u0000lp\u0001\u0000\u0000\u0000"+
		"mk\u0001\u0000\u0000\u0000np\u0001\u0000\u0000\u0000of\u0001\u0000\u0000"+
		"\u0000on\u0001\u0000\u0000\u0000pq\u0001\u0000\u0000\u0000qs\u0005\u000e"+
		"\u0000\u0000rb\u0001\u0000\u0000\u0000rc\u0001\u0000\u0000\u0000rd\u0001"+
		"\u0000\u0000\u0000st\u0001\u0000\u0000\u0000tu\u0005\u000e\u0000\u0000"+
		"uv\u0005\u0004\u0000\u0000vw\u0005\u0016\u0000\u0000wx\u0005\u0003\u0000"+
		"\u0000xy\u0005\u0016\u0000\u0000y{\u0005\u0018\u0000\u0000z=\u0001\u0000"+
		"\u0000\u0000zD\u0001\u0000\u0000\u0000z_\u0001\u0000\u0000\u0000{\u0011"+
		"\u0001\u0000\u0000\u0000|}\u0005\u000b\u0000\u0000}~\u0005\u0016\u0000"+
		"\u0000~\u007f\u0005\u0003\u0000\u0000\u007f\u0080\u0005\u0016\u0000\u0000"+
		"\u0080\u0081\u0005\u0018\u0000\u0000\u0081\u0013\u0001\u0000\u0000\u0000"+
		"\u0082\u0084\u0005\u0019\u0000\u0000\u0083\u0085\u0003\u0004\u0002\u0000"+
		"\u0084\u0083\u0001\u0000\u0000\u0000\u0085\u0086\u0001\u0000\u0000\u0000"+
		"\u0086\u0084\u0001\u0000\u0000\u0000\u0086\u0087\u0001\u0000\u0000\u0000"+
		"\u0087\u0088\u0001\u0000\u0000\u0000\u0088\u0089\u0005\u001a\u0000\u0000"+
		"\u0089\u0015\u0001\u0000\u0000\u0000\u008a\u008b\u0005\u0002\u0000\u0000"+
		"\u008b\u008c\u0003\u0018\f\u0000\u008c\u0017\u0001\u0000\u0000\u0000\u008d"+
		"\u008e\u0005\u0019\u0000\u0000\u008e\u0090\u0003\u001a\r\u0000\u008f\u0091"+
		"\u0003\u001a\r\u0000\u0090\u008f\u0001\u0000\u0000\u0000\u0091\u0092\u0001"+
		"\u0000\u0000\u0000\u0092\u0090\u0001\u0000\u0000\u0000\u0092\u0093\u0001"+
		"\u0000\u0000\u0000\u0093\u0094\u0001\u0000\u0000\u0000\u0094\u0095\u0005"+
		"\u001a\u0000\u0000\u0095\u0019\u0001\u0000\u0000\u0000\u0096\u0097\u0005"+
		"\u0016\u0000\u0000\u0097\u0098\u0005\u0018\u0000\u0000\u0098\u001b\u0001"+
		"\u0000\u0000\u0000\n*PTWkorz\u0086\u0092";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}